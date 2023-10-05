
from django.forms import ModelForm
from .models import Ingredients

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = (
            'food_item',
            'amount',
            'recipe',
        )
