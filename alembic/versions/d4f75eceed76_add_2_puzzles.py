"""add 2 puzzles

Revision ID: d4f75eceed76
Revises: 338097e53d1c
Create Date: 2020-05-06 13:20:52.102306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f75eceed76'
down_revision = '338097e53d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('puzzle_10', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('puzzle_11', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'puzzle_11')
    op.drop_column('users', 'puzzle_10')
    # ### end Alembic commands ###