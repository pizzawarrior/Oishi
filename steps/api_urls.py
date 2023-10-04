from django.urls import path
from steps.api_views import api_show_steps, api_step_list

urlpatterns = [
    # do we want a list steps????
    path('steps/', api_step_list, name='api_show_steps'),
    path('step/detail/<int:id>', api_show_steps, name='api_show_steps'),
]
