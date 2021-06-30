import time

from sqlalchemy import inspect
from unidecode import unidecode
from django.template.defaultfilters import slugify


def timestamp():
    return int(time.time())


def generate_slug(random_str):
    return slugify(unidecode(random_str))


def object_as_dict(obj):
    if obj:
        if isinstance(obj, list):
            object_dict_list = []
            for object in obj:
                object_dict = {c.key: getattr(object, c.key) for c in inspect(object).mapper.column_attrs}
                # if 'cp' in object_dict.keys():
                # del object_dict['cp']
                object_dict_list.append(object_dict)
            return object_dict_list
        else:
            object_dict = {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
            # if 'cp' in object_dict.keys():
            # del object_dict['cp']
            return object_dict
    return None