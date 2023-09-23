"""create post table

Revision ID: 83fa4072ffce
Revises: db8f5fe2a8f8
Create Date: 2023-09-22 20:50:54.484467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83fa4072ffce'
down_revision = 'db8f5fe2a8f8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
