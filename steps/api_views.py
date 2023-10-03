from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeStepForm
from .models import RecipeStep


@login_required(login_url="/accounts/login/")
def create_steps(request):
    if request.method == 'POST':
        form = RecipeStepForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('show_recipe')
            return redirect('recipe_list')
    else:
        form = RecipeStepForm()
    context = {'form': form}
    return render(request, 'steps/create.html', context)


@login_required(login_url="/accounts/login/")
def edit_steps(request, id):
    steps = get_object_or_404(RecipeStep, id=id)
    if request.method == 'POST':
        form = RecipeStepForm(request.POST, instance = steps)
        if form.is_valid():
            form.save()
            return redirect('show_recipe')
    else:
        form = RecipeStepForm(instance=steps)
    context = {
        'steps': steps,
        'form': form,
    }
    return render(request, 'steps/edit.html', context)


@login_required(login_url="/accounts/login/")
def show_steps(request):
    steps = RecipeStep.objects.filter(author=request.user)
    context = {'steps': steps}
    return render(request, 'steps/detail.html', context)
