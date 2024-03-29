"""removed game column from game data table

Revision ID: 002
Revises: 001
Create Date: 2021-06-26 22:19:54.252910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game_data', 'game')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_data', sa.Column('game', sa.TEXT(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
