from django.urls import path
from .api_views import api_show_ingredients


urlpatterns = [
    # do we want a ingredients/list/???
    path('ingredients/detail/<int:id>/', api_show_ingredients, name='api_show_ingredients')
]
