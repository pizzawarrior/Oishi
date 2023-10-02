from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

#create
@login_required(login_url='/accounts/login/')
def create_recipe(request):
    if request.method == 'POST':
        form  = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    context = {
        'form': form,

    }
    return render(request, 'recipes/create.html', context)

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


#edit/ update
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

#delete
def delete_recipe(request, id):
    query = Recipe.objects.get(id=id)
    query.delete()
    return HttpResponse("Recipe has been deleted!")

# alternative delete:
# def delete_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     recipe.delete()
#     return redirect('recipe_list')
