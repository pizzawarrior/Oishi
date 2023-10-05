from django.db import models
from recipes.models import Recipe
from django.urls import reverse


class RecipeStep(models.Model):
    instruction = models.TextField()
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        Recipe,
        related_name= 'steps',
        on_delete=models.CASCADE
    )

    def get_api_url(self):
        return reverse('api_show_steps', kwargs={'id': self.id})

        # Meta ordering may be less performant at scale, consider ordering using ORM
    class Meta:
        ordering= ['order']
