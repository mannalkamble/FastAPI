"""add content column to post table

Revision ID: 9b7b0d0d198d
Revises: 83fa4072ffce
Create Date: 2023-09-22 20:59:36.465582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b7b0d0d198d'
down_revision = '83fa4072ffce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts')
