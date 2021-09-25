from apps.models.coingecko.crypto_model import Crypto
from apps.models.coingecko.crypto_price_history import CryptoPriceHistory
from helper.helper import timestamp


class AddCrypto:
    @staticmethod
    def add_data(response_data):
        for price_history_dict in response_data:
            print("*"*40)
            print("price_history_dict")
            print(price_history_dict)
            print("*"*40)

            add_crypto_object = AddCrypto()

            for key, value in price_history_dict.items():
                setattr(add_crypto_object, key, value)

            crypto_object = add_crypto_object.add_crypto()
            crypto_price_history_object = add_crypto_object.add_crypto_price_history(crypto_object=crypto_object)

            print("crypto_object.id")
            print(crypto_object.id)
            print("crypto_price_history_object.id")
            print(crypto_price_history_object.id)

    def add_crypto(self):
        crypto_object = Crypto.get_by_slug(self.id)
        if not crypto_object:
            crypto_object = Crypto(
                name=self.name,
                symbol=self.symbol,
                slug=self.id,
                created_at=timestamp()
            ).add()
        return crypto_object

    def add_crypto_price_history(self, crypto_object):
        price_change_24h = {
            'price_change_24h': self.price_change_24h,
            'price_change_percentage_24h': self.price_change_percentage_24h
        }
        market_cap_change = {
            'market_cap_change_24h': self.market_cap_change_24h,
            'market_cap_change_percentage_24h': self.market_cap_change_percentage_24h
        }
        ath = {
            "ath": self.ath,
            "ath_change_percentage": self.ath_change_percentage,
            "ath_date": self.ath_date,
        }
        atl = {
            "atl": self.atl,
            "atl_change_percentage": self.atl_change_percentage,
            "atl_date": self.atl_date,
        }
        supply = {
            "circulating_supply": self.circulating_supply,
            "total_supply": self.total_supply,
            "max_supply": self.max_supply,
        }

        crypto_price_history_object = CryptoPriceHistory(
            crypto_id=crypto_object.id,
            rank=self.market_cap_rank,
            price=self.current_price,
            market_cap=self.market_cap,
            total_volume=self.total_volume,
            price_change_24h=price_change_24h,
            market_cap_change=market_cap_change,
            supply=supply,
            ath=ath,
            atl=atl,
            created_at=timestamp()
        ).add()
        return crypto_price_history_object