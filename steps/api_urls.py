from django.urls import path
from steps.api_views import create_steps, edit_steps, show_steps

urlpatterns = [
    path('steps/create/', create_steps, name='create_steps'),
    path('steps/edit/<int:id>/', edit_steps, name='edit_steps'),
    path('steps/detail/', show_steps, name='show_steps'),
]
