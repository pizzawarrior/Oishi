from django.contrib import admin

# Register your models here.
from recipes.models import Recipe, RecipeStep, Ingredients

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id'
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'instruction',
        'id'
    )

@admin.register(Ingredients)
class Ingredients(admin.ModelAdmin):
    list_display = (
        'amount',
        'food_item',
    )
