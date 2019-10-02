"""empty message

Revision ID: 84600512f636
Revises: a563e88e5f25
Create Date: 2019-10-01 22:17:29.449750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84600512f636'
down_revision = 'a563e88e5f25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
