from django.db import models
from recipes.models import Recipe

class Ingredients(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)

    recipe = models.ForeignKey(
        Recipe,
        related_name= 'ingredients',
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering= ['food_item']
