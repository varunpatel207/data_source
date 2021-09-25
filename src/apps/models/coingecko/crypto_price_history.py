from sqlalchemy import Column, BigInteger, Float
from sqlalchemy.dialects.postgresql import JSONB

from apps.models.base import BaseModel, session
from apps.models.coingecko.crypto_model import Crypto


class CryptoPriceHistory(BaseModel):
    __tablename__ = "crypto_price_history"
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    crypto_id = Column(BigInteger, nullable=False)
    rank = Column(BigInteger, nullable=False)
    price = Column(Float, nullable=False)
    market_cap = Column(Float, nullable=False)
    total_volume = Column(Float, nullable=False)
    price_change_24h = Column(JSONB)
    market_cap_change = Column(JSONB)
    supply = Column(JSONB)
    ath = Column(JSONB)
    atl = Column(JSONB)
    created_at = Column(BigInteger, nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def search(cls):
        result_query = session.query(CryptoPriceHistory, Crypto).join(Crypto, Crypto.id == CryptoPriceHistory.crypto_id)
        result = result_query.all()
        return result

