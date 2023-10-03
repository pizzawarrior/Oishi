from django.urls import path
from recipes.api_views import api_show_recipe, api_recipe_list, create_recipe, edit_recipe, delete_recipe, my_recipe_list

urlpatterns = [
    path('recipes/create/', create_recipe, name='create_recipe'),
    path('recipes/', api_recipe_list, name= 'recipe_list'),
    path('recipes/<int:id>/', api_show_recipe, name= 'show_recipe'),
    path('recipes/<int:id>/edit/', edit_recipe, name='edit_recipe'),
    path('recipes/<int:id>/delete/', delete_recipe, name='delete_recipe'),
    path('recipes/mine/', my_recipe_list, name='my_recipe_list')

]
