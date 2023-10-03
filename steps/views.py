from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeStepForm

# Create your views here.
@login_required(login_url="/accounts/login/")
def create_steps(request):
    if request.method == 'POST':
        form = RecipeStepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_recipe')
    else:
        form = RecipeStepForm()
    context = {form: form}
    return render(request, 'steps/create.html', context)
