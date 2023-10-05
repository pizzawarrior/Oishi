from django.db import models
from django.urls import reverse


class RecipeVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class Ingredients(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)

    recipe = models.ForeignKey(
        RecipeVO,
        related_name= 'ingredients',
        on_delete=models.CASCADE,
    )

    def get_api_url(self):
        return reverse("api_show_ingredients", kwargs={"id": self.id})

    class Meta:
        ordering= ['food_item']
