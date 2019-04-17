"""empty message

Revision ID: 820fafb70c8c
Revises: fd94d0292e7f
Create Date: 2019-04-16 17:43:16.391546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '820fafb70c8c'
down_revision = 'fd94d0292e7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('is_active_string', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'is_active_string')
    # ### end Alembic commands ###