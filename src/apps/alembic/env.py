import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, MetaData
from sqlalchemy import pool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 'src/apps'
APPS_PATH = os.path.join(BASE_DIR, '..')
sys.path.append(APPS_PATH)

config = context.config

fileConfig(config.config_file_name)

from twitch import settings

import apps.models.game_data_model as game_data
import apps.models.game_model as game
import apps.models.android_app_model as android_app
import apps.models.coingecko.crypto_model as crypto_model
import apps.models.coingecko.crypto_price_history as crypto_price_history

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


DATABASE_NAME = settings.DATABASES['default']['NAME']
DB_USERNAME = settings.DATABASES['default']['USER']
DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
DB_HOST = settings.DATABASES['default']['HOST']
SQLALCHEMY_URL = "postgresql+psycopg2://" + DB_USERNAME + ":" + DB_PASSWORD + '@' + DB_HOST + '/' + DATABASE_NAME


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m


target_metadata = combine_metadata(game_data.BaseModel.metadata, game.BaseModel.metadata,
                                   android_app.BaseModel.metadata, crypto_model.BaseModel.metadata,
                                   crypto_price_history.BaseModel.metadata)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
