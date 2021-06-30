from sqlalchemy import Column, BigInteger, Text, Integer, Float

from apps.models.base import BaseModel, session
from apps.models.game_model import Game
from helper.constants import PAGINATION_LIMIT


class GameData(BaseModel):
    __tablename__ = "game_data"
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    rank = Column(Integer, nullable=False)
    game_id = Column(BigInteger, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    hours_watched = Column(BigInteger, nullable=True)
    hours_streamed = Column(BigInteger, nullable=True)
    peak_viewers = Column(BigInteger, nullable=True)
    peak_channels = Column(BigInteger, nullable=True)
    streamers = Column(BigInteger, nullable=True)
    avg_viewers = Column(BigInteger, nullable=True)
    avg_channels = Column(BigInteger, nullable=True)
    avg_viewer_ratio = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def search_game(**kwargs):
        game_id = kwargs.get('game_id')
        month = kwargs.get('month')
        year = kwargs.get('year')
        page = kwargs.get('page')

        game_data_query = session.query(GameData)

        if game_id:
            game_data_query = game_data_query.filter(GameData.game_id == game_id)

        if month:
            game_data_query = game_data_query.filter(GameData.month == month)

        if year:
            game_data_query = game_data_query.filter(GameData.year == year)

        if isinstance(page, int):
            game_data_query = game_data_query.offset(page * PAGINATION_LIMIT).limit(PAGINATION_LIMIT)

        game_result = game_data_query.all()
        print(game_data_query)
        count = game_data_query.count()

        return game_result, count

    def game_filter(**kwargs):
        game_slug = kwargs.get('game_slug')
        page = kwargs.get('page')

        game_data_query = session.query(GameData, Game).join(Game, GameData.game_id == Game.id)

        if game_slug:
            game_data_query = game_data_query.query(Game.slug == game_slug)

        if isinstance(page, int):
            game_data_query = game_data_query.offset(page * PAGINATION_LIMIT).limit(PAGINATION_LIMIT)

        game_result = game_data_query.all()
        count = game_data_query.count()

        return game_result, count

    @staticmethod
    def bulk_add(game_object_list):
        session.bulk_save_objects(game_object_list)
        session.commit()
        return True