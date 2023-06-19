"""add phone number

Revision ID: 64efd859725f
Revises: 648b88812133
Create Date: 2023-06-19 20:20:53.023462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64efd859725f'
down_revision = '648b88812133'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
