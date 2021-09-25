from sqlalchemy import Column, BigInteger, Integer, Float, Text, String, Boolean, func

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

    def search(self, **kwargs):
        category = kwargs.get('category')
        installs = kwargs.get('installs')
        total_ratings = kwargs.get('total_ratings')
        paid = kwargs.get('paid')

        result_query = session.query(AndroidApp)
        count_query = session.query(AndroidApp)

        if category:
            result_query = result_query.filter(AndroidApp.category == category)
            count_query = count_query.filter(AndroidApp.category == category)

        if installs:
            result_query = result_query.filter(AndroidApp.installs >= installs)
            count_query = count_query.filter(AndroidApp.installs >= installs)

        if total_ratings:
            result_query = result_query.filter(AndroidApp.total_ratings >= total_ratings)
            count_query = count_query.filter(AndroidApp.total_ratings >= total_ratings)

        if paid:
            result_query = result_query.filter(AndroidApp.paid == paid)
            count_query = count_query.filter(AndroidApp.paid == paid)

        results = result_query.order_by(AndroidApp.id.desc()).limit().all()
        total_count = count_query.order_by(AndroidApp.id.desc()).all()
        return results, total_count
