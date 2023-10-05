# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from django.http import HttpResponse

from django.http import JsonResponse
import json
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
from .acls import get_image


# # create recipe
# @login_required(login_url='/accounts/login/')
# def create_recipe(request):
#     if request.method == 'POST':
#         form  = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save(False)
#             recipe.author = request.user
#             recipe.save()
#             return redirect('recipe_list')
#     else:
#         form = RecipeForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'recipes/create.html', context)


# # No worky: need some way to indicate current user == author
# # USER SPECIFIC FILTERED RECIPE LIST
# def api_my_recipe_list(request, author_id):
#     recipes = [
#         {
#             'title': r.title,
#         }
#         for r in Recipe.objects.filter(author=author_id)
#     ]
#     return JsonResponse({'recipes': recipes})


class RecipeDetailEncoder(ModelEncoder):
    model = Recipe
    properties = [
        'title',
        'picture',
        'description',
        'rating',
        'created_on'
    ]

class RecipeListEncoder(ModelEncoder):
    model = Recipe
    properties = [
        'title',
    ]

# my recipe list:
@require_http_methods(['GET', 'POST'])
def api_my_recipe_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.filter(author=request.user.id)
        return JsonResponse(
            {'recipe': recipe},
            encoder=RecipeListEncoder,
            safe=False
            )
    else:
        content = json.loads(request.body)

        # the property in get_image may need to be altered
        picture = get_image(content['title'])
        content.update(picture)

        recipe = Recipe.objects.create(**content)
        return JsonResponse(
            recipe,
            encoder=RecipeDetailEncoder,
            safe=False,
        )



# OLD: this is from before using the model encoders
# # USER SPECIFIC FILTERED RECIPE LIST
# def api_my_recipe_list(request):
#     response = []
#     recipes = Recipe.objects.filter(author=request.user.id)
#     for recipe in recipes:
#         response.append(
#             {
#                 'title': recipe.title,
#             }
#         )
#     return JsonResponse({'recipes': response})


#list ALL recipes
@require_http_methods(['GET', 'POST'])
def api_recipe_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        return JsonResponse(
            {'recipe': recipe},
            encoder=RecipeListEncoder,
            safe=False
            )
    else:
        content = json.loads(request.body)

        # the property in get_image may need to be altered
        picture = get_image(content['title'])
        content.update(picture)

        recipe = Recipe.objects.create(**content)
        return JsonResponse(
            recipe,
            encoder=RecipeDetailEncoder,
            safe=False,
        )


# OLD: Before encoders
# #list ALL recipes
# def api_recipe_list(request):
#     response = []
#     recipes = Recipe.objects.all()
#     for recipe in recipes:
#         response.append(
#             {
#                 'title': recipe.title,
#                 # 'href': recipe.get_api_url()
#             }
#         )
#     return JsonResponse({'recipes': response})


# show recipe detail
@require_http_methods(['GET', 'PUT', 'DELETE'])
def api_show_recipe(request, id):
    if request.method == 'GET':
        recipe = Recipe.objects.get(id=id)
        return JsonResponse(
            recipe,
            encoder=RecipeDetailEncoder,
            safe=False
        )
    elif request.method == 'DELETE':
        count, _ = Recipe.objects.filter(id=id).delete()
        return JsonResponse({'deleted': count > 0})
    else:
        content = json.loads(request.body)
        Recipe.objects.filter(id=id).update(**content)
        recipe = Recipe.objects.get(id=id)
        return JsonResponse(
            recipe,
            encoder=RecipeDetailEncoder,
            safe=False,
        )


# # OLD, show recipe detail -- BEFORE MAKING A MODEL ENCODER::::
# def api_show_recipe(request, id):
#     recipe = Recipe.objects.get(id=id)
#     return JsonResponse(
#         {
#             'title': recipe.title,
#             'picture': recipe.picture,
#             'description': recipe.description,
#             'rating': recipe.rating
#         }
#     )

# OLD Remainders of CRUD from when we were using templates
# #edit/ update recipe
# def edit_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, instance = recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('show_recipe', id=id)
#     else:
#         form = RecipeForm(instance = recipe)
#     context = {
#         'recipe': recipe,
#         'form': form,
#         }
#     return render(request, 'recipes/edit.html', context)


# #delete recipe
# def delete_recipe(request, id):
#     query = Recipe.objects.get(id=id)
#     query.delete()
#     return HttpResponse("Recipe has been deleted!")