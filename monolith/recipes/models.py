from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# rating validation:
def validate_integer(value):
    if value > 5:
        raise ValidationError(
            _('Pick a number between 0 and 5'),
            params={'value': value},
        )

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(validators=[validate_integer])

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_api_url(self):
        return reverse('api_show_recipe', kwargs={'id': self.id})
