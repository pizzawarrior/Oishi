import json
import requests
from .models import RecipeVO

# this uses crontab to routinely pull in recipes from the API on a set schedule
def get_recipes():
    url = "http://monolith:8000/api/recipes/"
    response = requests.get(url)
    content = json.loads(response.content)
    for recipe in content["recipes"]:
        RecipeVO.objects.update_or_create(
            import_href=recipe["href"],
            defaults={"title": recipe["title"]},
        )
