from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IngredientsForm

# Create your views here.
@login_required(login_url="/accounts/login/")
def add_ingredients(request):
    if request.method == 'POST':
        form = IngredientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_recipe')
    else:
        form = IngredientsForm()
    context = {form: form}
    return render(request, 'ingredients/create.html', context)
