from django.urls import path
from .api_views import add_ingredients, edit_ingredients, show_ingredients

urlpatterns = [
    path('ingredients/create/', add_ingredients, name='add_ingredients'),
    path('ingredients/edit/<int:id>/', edit_ingredients, name='edit_ingredients'),
    path('ingredients/detail/', show_ingredients, name='show_ingredients')
]
