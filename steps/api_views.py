from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RecipeStep
from recipes.models import Recipe
from django.http import JsonResponse
import json
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods


# Back from when we were using templatesand forms to transfer data:
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


# Back from when we were using templatesand forms to transfer data:
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


class RecipeStepEncoder(ModelEncoder):
    model = RecipeStep
    properties = [
        'instruction',
        'order',
    ]


@require_http_methods(['GET', 'POST'])
def api_step_list(request):
    if request.method == 'GET':
        step = RecipeStep.objects.all()
        return JsonResponse(
            {'step': step},
            encoder=RecipeStepEncoder,
            safe=False
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
        step = RecipeStep.objects.create(**content)
        return JsonResponse(
            step,
            encoder=RecipeStepEncoder,
            safe=False
        )


# OLD:
# def api_step_list(request):
#     step = RecipeStep.objects.all()
#     return JsonResponse(
#         {'step': step},
#         encoder=RecipeStepEncoder,
#         safe=False
#     )


# # OLD, from before encoders
# # show list of steps
# def api_step_list(request):
#     response = []
#     steps = RecipeStep.objects.all()
#     for step in steps:
#         response.append(
#             {
#                 'instruction': step.instruction,
#                 'order': step.order,
#             }
#         )
#     return JsonResponse({'steps': response})


# show step detail
@require_http_methods(['DELETE', 'GET', 'PUT'])
def api_show_steps(request, id):
    if request.method == 'GET':
        step = RecipeStep.objects.get(id=id)
        return JsonResponse(
            step,
            encoder=RecipeStepEncoder,
            safe=False,
        )
    elif request.method == 'DELETE':
        count, _ = RecipeStep.objects.filter(id=id).delete()
        return JsonResponse({'deleted': count > 0})
    else:
        content = json.loads(request.body)
        RecipeStep.objects.filter(id=id).update(**content)
        step = RecipeStep.objects.get(id=id)
        return JsonResponse(
            step,
            encoder=RecipeStepEncoder,
            safe=False
        )




# # show step detail
# def api_show_steps(request, id):
#     step = RecipeStep.objects.get(id=id)
#     return JsonResponse(
#         step,
#         encoder=RecipeStepEncoder,
#         safe=False,
#     )


# OLD: before using detail encoder
# # show step detail
# def api_show_steps(request, id):
#     steps = RecipeStep.objects.get(id=id)
#     return JsonResponse(
#         {
#             'instruction': steps.instruction,
#             'order': steps.order,
#         }
#     )
