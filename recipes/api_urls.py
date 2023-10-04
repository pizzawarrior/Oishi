from django.urls import path
from recipes.api_views import (
    api_show_recipe,
    api_recipe_list,
    api_my_recipe_list
)

urlpatterns = [
    path('recipes/', api_recipe_list, name= 'api_recipe_list'),
    path('recipes/<int:id>/', api_show_recipe, name= 'api_show_recipe'),
    path('recipes/mine/', api_my_recipe_list, name='api_my_recipe_list'),

]
