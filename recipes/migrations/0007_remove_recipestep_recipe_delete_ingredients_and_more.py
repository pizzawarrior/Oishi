# Generated by Django 4.2.5 on 2023-10-03 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipestep',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='RecipeStep',
        ),
    ]
