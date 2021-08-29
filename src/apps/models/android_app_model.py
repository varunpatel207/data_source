from sqlalchemy import Column, BigInteger, Integer, Float, Text, String, Boolean

from apps.models.base import session, BaseModel


class AndroidApp(BaseModel):
    __tablename__ = "android_app"
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    rank = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    total_ratings = Column(BigInteger, nullable=True)
    installs = Column(Float, nullable=True)
    avg_rating = Column(BigInteger, nullable=True)
    growth_30day = Column(Float, nullable=True)
    growth_60day = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    category = Column(String(255), nullable=True)
    rating_5 = Column(BigInteger, nullable=True)
    rating_4 = Column(BigInteger, nullable=True)
    rating_3 = Column(BigInteger, nullable=True)
    rating_2 = Column(BigInteger, nullable=True)
    rating_1 = Column(BigInteger, nullable=True)
    paid = Column(Boolean, nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def bulk_add(cls, game_object_list):
        session.bulk_save_objects(game_object_list)
        session.commit()
        return True
