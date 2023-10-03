from django.forms import ModelForm
from recipes.models import Recipe, Ingredients, RecipeStep

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'picture',
            'description',
            'rating'
        )

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = (
            'food_item',
            'amount'
        )

class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = (
            'instruction',
            'order'
        )
