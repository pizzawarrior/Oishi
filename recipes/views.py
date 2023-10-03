from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm, IngredientsForm, RecipeStepForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#create recipe
@login_required(login_url='/accounts/login/')
def create_recipe(request):
    if request.method == 'POST':
        recipe_form  = RecipeForm(request.POST)
        ingredients_form = IngredientsForm(request.POST)
        recipe_step_form = RecipeStepForm(request.POST)
        if all([recipe_form.is_valid() and ingredients_form.is_valid() and recipe_step_form.is_valid()]):
            recipe_form = recipe_form.save(False)
            recipe_form.author = request.user
            ing = ingredients_form.save()
            rec_step = recipe_step_form.save()
            rec = recipe_form.save()

            ing.ingredients = ing
            rec_step.steps = rec_step
            rec.save()

            messages.success(request, "Your profile was successfully updated!")
            return redirect('recipe_list')

    else:
        messages.error(request, "Please correct the error below.")
        recipe_form = RecipeForm()
        ingredients_form = IngredientsForm()
        recipe_step_form = RecipeStepForm()

    context = {
        'recipe_form': recipe_form,
        'ingredients_form': ingredients_form,
        'recipe_step_form': recipe_step_form,

    }
    return render(request, 'recipes/create.html', context)


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


# USER SPECIFIC FILTERED LIST
@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author = request.user)
    context = {
        'recipe_list': recipes
    }
    return render(request, 'recipes/list.html', context)


#list
def recipe_list(request):
    recipe = Recipe.objects.all()
    context = {
        'recipe_list': recipe,
    }
    return render(request, 'recipes/list.html', context)


#detail
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe_object': recipe,
    }
    return render(request, 'recipes/detail.html', context)


#edit/ update recipe
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance = recipe)
        if form.is_valid():
            form.save()
            return redirect('show_recipe', id=id)
    else:
        form = RecipeForm(instance = recipe)
    context = {
        'recipe': recipe,
        'form': form,
        }
    return render(request, 'recipes/edit.html', context)


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

#delete recipe
def delete_recipe(request, id):
    query = Recipe.objects.get(id=id)
    query.delete()
    return HttpResponse("Recipe has been deleted!")
