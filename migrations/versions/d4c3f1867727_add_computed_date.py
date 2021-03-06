"""add computed date

Revision ID: d4c3f1867727
Revises: 93ff4335d83d
Create Date: 2020-07-22 17:42:15.000910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4c3f1867727'
down_revision = '93ff4335d83d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dataset', sa.Column('computed', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dataset', 'computed')
    # ### end Alembic commands ###
