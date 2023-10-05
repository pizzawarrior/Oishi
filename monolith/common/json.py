from json import JSONEncoder
from datetime import datetime
from typing import Any
from django.db.models import QuerySet


# this is for handling errors when we create list views in our views files and a QuerySet object is returned
class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


# JSON does not like dates! So we do this:
class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)


class ModelEncoder(DateEncoder, QuerySetEncoder, JSONEncoder):
    def default(self, o):
        #   if the object to decode is the same class as what's in the
        #   model property, then
        if isinstance(o, self.model):
        #     * create an empty dictionary that will hold the property names
        #       as keys and the property values as values
            result = {}
            # if o has the attribute get_api_url
            if hasattr(o, 'get_api_url'):
            #    then add its return value to the dictionary
            #    with the key "href"
                result['href'] = o.get_api_url()
        #     * for each name in the properties list
            for prop in self.properties:
        #         * get the value of that property from the model instance
        #           given just the property name
                value = getattr(o, prop)
        #         * put it into the dictionary with that property name as
        #           the key
                result[prop] = value
        #     * return the dictionary
            return result
        #   otherwise,
        else:
        #       return super().default(o)  # From the documentation
            return super().default(o)
