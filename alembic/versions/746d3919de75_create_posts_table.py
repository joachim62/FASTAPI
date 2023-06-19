"""create posts table

Revision ID: 746d3919de75
Revises: 
Create Date: 2023-06-18 12:35:44.940174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '746d3919de75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                                       primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
