from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ingredients
from recipes.models import Recipe
from django.http import JsonResponse
import json


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


def api_show_ingredients(request, id):
    ingredient = Ingredients.objects.get(id=id)
    return JsonResponse(
        {
            'food_item': ingredient.food_item,
            'amount': ingredient.amount,
        }
    )
