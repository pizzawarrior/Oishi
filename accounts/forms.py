from django import forms
from django.contrib.auth import authenticate, login

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=50,
        # override default <input type='text>
        widget=forms.PasswordInput,
        )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=50,
        # override default <input type='text>
        widget=forms.PasswordInput,
        )
