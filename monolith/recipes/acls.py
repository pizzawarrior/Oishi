from .keys import PEXELS_API_KEY
import requests
import json

def get_image(title):
    url = 'https://api.pexels.com/v1/search'
    headers = {'Authorization': PEXELS_API_KEY}
    params = {
        'query': f"{title}",
        'per_page': 1
    }
    response = requests.get(url, headers=headers, params=params)
    # picture = json.loads(response.content)
    parsed_json = json.loads(response.content)
    print(parsed_json)
    picture = parsed_json['photos'][0]['src']['original']
    return {
        'picture': picture
    }
