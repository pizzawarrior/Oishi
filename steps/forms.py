from django.forms import ModelForm
from .models import RecipeStep

class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = (
            'instruction',
            'order'
        )
