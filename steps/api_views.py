from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RecipeStep
from django.http import JsonResponse
import json
from common.json import ModelEncoder


# @login_required(login_url="/accounts/login/")
# def create_steps(request):
#     if request.method == 'POST':
#         form = RecipeStepForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('show_recipe')
#             return redirect('recipe_list')
#     else:
#         form = RecipeStepForm()
#     context = {'form': form}
#     return render(request, 'steps/create.html', context)


# @login_required(login_url="/accounts/login/")
# def edit_steps(request, id):
#     steps = get_object_or_404(RecipeStep, id=id)
#     if request.method == 'POST':
#         form = RecipeStepForm(request.POST, instance = steps)
#         if form.is_valid():
#             form.save()
#             return redirect('show_recipe')
#     else:
#         form = RecipeStepForm(instance=steps)
#     context = {
#         'steps': steps,
#         'form': form,
#     }
#     return render(request, 'steps/edit.html', context)


# show list of steps
def api_step_list(request):
    response = []
    steps = RecipeStep.objects.all()
    for step in steps:
        response.append(
            {
                'instruction': step.instruction,
                'order': step.order,
            }
        )
    return JsonResponse({'steps': response})


# show step detail
def api_show_steps(request, id):
    steps = RecipeStep.objects.get(id=id)
    return JsonResponse(
        {
            'instruction': steps.instruction,
            'order': steps.order,
            # 'recipe': steps.recipe
        }
    )
