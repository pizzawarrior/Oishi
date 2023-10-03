from django.db import models
from recipes.models import Recipe
from django.urls import reverse

class Ingredients(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)

    recipe = models.ForeignKey(
        Recipe,
        related_name= 'ingredients',
        on_delete=models.CASCADE,
    )

    def get_api_url(self):
        return reverse("api_show_ingredients", kwargs={"id": self.id})

    class Meta:
        ordering= ['food_item']
