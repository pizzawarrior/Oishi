from django.urls import path
from .api_views import api_ingredients_list, api_show_ingredients


urlpatterns = [
    # path('recipes/<int:id>/ingredients/', api_ingredients_list, name='api_ingredients_list'),
    path('ingredients/', api_ingredients_list, name='api_ingredients_list'),
    path('ingredients/<int:id>/', api_show_ingredients, name='api_show_ingredients'),
]
