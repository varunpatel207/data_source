from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url('game', include('apps.urls.game_urls', namespace='game')),
]
