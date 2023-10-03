from django.urls import path
from .views import add_ingredients

urlpatterns = [
    path('create/', add_ingredients, name='add_ingredients'),
]
