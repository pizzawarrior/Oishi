from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import SignUpForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create user with values from above:
            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password = password,
                    first_name = first_name,
                    last_name = last_name
                )
                # Log user in:
                login(request, user)

                return redirect('recipe_list')
                # return HttpResponse('You are logged in!')???
            else:
                form.add_error('password', 'Passwords do not match')

    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password
        )
            if user is not None:
                login(request, user)
                return redirect('recipe_list')
    else:
        form = LoginForm()
        context = {
            'form': form
    }
    return render(request, 'accounts/login.html', context)



def user_logout(request):
    logout(request)
    return redirect('recipe_list')
