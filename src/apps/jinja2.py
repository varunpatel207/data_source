from datetime import datetime
import math
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

from twitch.settings import BASE_URL


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'base_url': BASE_URL
        ,
        'current_timestamp': math.ceil(datetime.now().timestamp())
    }, zip = zip)
    return env
