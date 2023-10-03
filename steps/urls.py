from django.urls import path
from steps.views import create_steps, edit_steps, show_steps

urlpatterns = [
    path('create/', create_steps, name='create_steps'),
    path('edit/<int:id>/', edit_steps, name='edit_steps'),
    path('detail/', show_steps, name='show_steps'),
]
