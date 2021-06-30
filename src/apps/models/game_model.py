from sqlalchemy import Column, BigInteger, Text, Integer, Float

from apps.models.base import BaseModel, session


class Game(BaseModel):
    __tablename__ = "game"
    __table_args__ = {'extend_existing': True}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    game = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def search_game(**kwargs):
        game = kwargs.get('game')
        game_query = session.query(Game)

        if game:
            game_query = game_query.filter(Game.game == game)

        game_result = game_query.all()
        count = game_query.count()

        return game_result, count

    @staticmethod
    def get_by_slug(slug):
        return session.query(Game).filter(Game.slug == slug).first()

    @staticmethod
    def bulk_add(game_object_list):
        session.bulk_save_objects(game_object_list)
        session.commit()
        return True