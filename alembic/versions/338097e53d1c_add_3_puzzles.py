"""add 3 puzzles

Revision ID: 338097e53d1c
Revises: de08e605e0cb
Create Date: 2020-05-06 12:16:02.703870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '338097e53d1c'
down_revision = 'de08e605e0cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('puzzle_7', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('puzzle_8', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('puzzle_9', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'puzzle_9')
    op.drop_column('users', 'puzzle_8')
    op.drop_column('users', 'puzzle_7')
    # ### end Alembic commands ###
