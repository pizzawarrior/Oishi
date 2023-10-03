from django.urls import path
from steps.views import create_steps

urlpatterns = [
    path('create/', create_steps, name='create_steps'),
]
