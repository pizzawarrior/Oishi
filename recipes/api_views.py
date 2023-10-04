from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


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


# # USER SPECIFIC FILTERED RECIPE LIST
def api_my_recipe_list(request):
    response = []
    recipes = Recipe.objects.filter(author=request.user.id)
    for recipe in recipes:
        response.append(
            {
                'title': recipe.title,
            }
        )
    return JsonResponse({'recipes': response})


#list ALL recipes
def api_recipe_list(request):
    response = []
    recipes = Recipe.objects.all()
    for recipe in recipes:
        response.append(
            {
                'title': recipe.title,
                # 'href': recipe.get_api_url()
            }
        )
    return JsonResponse({'recipes': response})


# show recipe detail
def api_show_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return JsonResponse(
        {
            'title': recipe.title,
            'picture': recipe.picture,
            'description': recipe.description,
            'rating': recipe.rating
        }
    )


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
