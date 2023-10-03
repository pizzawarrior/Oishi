from django.contrib import admin
from .models import RecipeStep

# Register your models here.
@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'instruction',
        'id'
    )
