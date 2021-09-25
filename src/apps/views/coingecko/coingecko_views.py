import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

from apps.models.coingecko.crypto_price_history import CryptoPriceHistory
from apps.views.coingecko.add_crypto_object import AddCrypto
from helper.helper import object_as_dict
from twitch.settings import COINGECKO_API_URL


class CoinGeckoViews:
    def get_daily_top_500(request):
        url = COINGECKO_API_URL + '/coins/markets'

        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 250,
            'price_change_percentage': '1h, 24h'
        }

        for page in range(1, 5):
            params.update({
                'page': page
            })
            try:
                response_data = requests.get(url, params=params)
                if response_data.status_code == 200:
                    response_data = json.loads(response_data.text)
                    AddCrypto.add_data(response_data=response_data)
            except Exception as e:
                print(e)
        return HttpResponse("Done")

    def get_all(request):
        context = {}

        crypto_history = CryptoPriceHistory.search()

        print("*"*40)
        print("crypto_history")
        print(crypto_history)
        print("*"*40)

        crypto_dict = {}
        history_dict = {}
        for history_object, crypto_object in crypto_history:
            history_dict[history_object.id] = object_as_dict(history_object)
            crypto_dict[crypto_object.id] = object_as_dict(crypto_object)
        context['crypto_history'] = history_dict
        context['crypto'] = crypto_dict
        return render(request, "coingecko/list.html", context)
