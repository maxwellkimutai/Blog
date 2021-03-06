"""add date column on posts table

Revision ID: 0592b3295882
Revises: d1a4cb34663c
Create Date: 2018-10-20 12:51:16.719254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0592b3295882'
down_revision = 'd1a4cb34663c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('date_posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'date_posted')
    # ### end Alembic commands ###
