from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ingredients
from recipes.models import Recipe
from django.http import JsonResponse
import json
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods


# @login_required(login_url="/accounts/login/")
# def add_ingredients(request):
#     if request.method == 'POST':
#         form = IngredientsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('show_recipe')
#             return redirect('recipe_list')
#     else:
#         form = IngredientsForm()
#     context = {'form': form}
#     return render(request, 'ingredients/create.html', context)


# @login_required(login_url="/accounts/login/")
# def edit_ingredients(request, id):
#     ingredients = get_object_or_404(Ingredients, id=id)
#     print(ingredients)
#     if request.method == 'POST':
#         form = IngredientsForm(request.POST, instance = ingredients)
#         if form.is_valid():
#             form.save()
#             return redirect('show_recipe')
#     else:
#         form = IngredientsForm(instance=ingredients)
#     context = {
#         'ingredients': ingredients,
#         'form': form,
#     }
#     return render(request, 'ingredients/edit.html', context)


# @login_required(login_url="/accounts/login/")
# def show_ingredients(request, id):
#     ingredients = get_object_or_404(Ingredients, id=id)
#     context = {'ingredients': ingredients}

#     return render(request, 'ingredients/detail.html', context)


class IngredientsDetailEncoder(ModelEncoder):
    model = Ingredients
    properties = [
        'food_item',
        'amount',

    ]
# POST is not working due to not being able to sync the recipe id with the ingredient
#  the result in Insomnia is a 'keyerror'
@require_http_methods(['GET', 'POST'])
def api_ingredients_list(request):
    if request.method == 'GET':
        ingredient = Ingredients.objects.all()
        return JsonResponse(
            {'ingredient': ingredient},
            encoder=IngredientsDetailEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            recipe = Recipe.objects.get(id=content['recipe'])
            content['recipe'] = recipe
        except Recipe.DoesNotExist:
            return JsonResponse(
                {'message': 'Invalid recipe id'},
                status=400
            )
        ingredient = Ingredients.objects.create(**content)
        return JsonResponse(
            ingredient,
            encoder=IngredientsDetailEncoder,
            safe=False
        )


# show ingredient detail, update, delete
@require_http_methods(['GET', 'PUT', 'DELETE'])
def api_show_ingredients(request, id):
    if request.method == 'GET':
        ingredient = Ingredients.objects.get(id=id)
        return JsonResponse(
            ingredient,
            encoder=IngredientsDetailEncoder,
            safe=False
        )
    elif request.method == 'DELETE':
        count, _ = Ingredients.objects.filter(id=id).delete()
        return JsonResponse({'deleted': count > 0})
    else:
        content = json.loads(request.body)
        Ingredients.objects.filter(id=id).update(**content)
        ingredient = Ingredients.objects.get(id=id)
        return JsonResponse(
            ingredient,
            encoder=IngredientsDetailEncoder,
            safe=False,
        )



# OLD: before using the encoder::::
# def api_show_ingredients(request, id):
#     ingredient = Ingredients.objects.get(id=id)
#     return JsonResponse(
#         {
#             'food_item': ingredient.food_item,
#             'amount': ingredient.amount,
#         }
#     )
