"""user tokens

Revision ID: b0738f3203a8
Revises: 8f8cfb1c44ac
Create Date: 2018-02-14 18:03:39.307773

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b0738f3203a8"
down_revision = "8f8cfb1c44ac"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("token", sa.String(length=32), nullable=True))
    op.add_column("user", sa.Column("token_expiration", sa.DateTime(), nullable=True))
    op.create_index(op.f("ix_user_token"), "user", ["token"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_token"), table_name="user")
    op.drop_column("user", "token_expiration")
    op.drop_column("user", "token")
    # ### end Alembic commands ###
