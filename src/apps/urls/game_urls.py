from django.conf.urls import url

from apps.views.game_views import GameViews

app_name = "game"

urlpatterns = [
    url('/upload-game-data', GameViews.upload_game_data, name='upload-game-data'),
    url('/game-info', GameViews.game_info, name='game-info'),
    url('', GameViews.dashboard, name='dashboard'),
]
