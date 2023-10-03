from django.urls import path
from .views import add_ingredients, edit_ingredients, show_ingredients

urlpatterns = [
    path('create/', add_ingredients, name='add_ingredients'),
    path('edit/<int:id>/', edit_ingredients, name='edit_ingredients'),
    # path('edit/', edit_ingredients, name='edit_ingredients'),
    path('detail/', show_ingredients, name='show_ingredients')
]
