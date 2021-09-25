from django.urls import path

from apps.views.coingecko.coingecko_views import CoinGeckoViews

app_name = "coingecko"

urlpatterns = [
    path('', CoinGeckoViews.get_all, name='get-all'),
    path('/get-data', CoinGeckoViews.get_daily_top_500, name='get-daily-top-500'),
]
