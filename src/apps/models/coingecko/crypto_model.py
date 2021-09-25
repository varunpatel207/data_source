from sqlalchemy import Column, BigInteger, String

from apps.models.base import BaseModel


class Crypto(BaseModel):
    __tablename__ = "crypto"
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    symbol = Column(String(50), nullable=False)
    slug = Column(String(100), nullable=False)
    created_at = Column(BigInteger, nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
