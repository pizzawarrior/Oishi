from django.contrib import admin
from .models import Ingredients

# Register your models here.
@admin.register(Ingredients)
class Ingredients(admin.ModelAdmin):
    list_display = (
        'amount',
        'food_item',
    )
