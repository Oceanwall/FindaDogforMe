"""empty message

Revision ID: b34d4763c087
Revises: d64020cb6abc
Create Date: 2019-03-19 23:42:15.814327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b34d4763c087"
down_revision = "d64020cb6abc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dog",
        sa.Column("id", sa.String(length=50), nullable=False),
        sa.Column("shelter_id", sa.String(length=50), nullable=True),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("breed", sa.String(length=255), nullable=True),
        sa.Column("age", sa.String(length=50), nullable=True),
        sa.Column("size", sa.String(length=50), nullable=True),
        sa.Column("sex", sa.String(length=50), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("image_1", sa.String(length=1000), nullable=True),
        sa.Column("image_2", sa.String(length=1000), nullable=True),
        sa.Column("image_3", sa.String(length=1000), nullable=True),
        sa.Column("image_4", sa.String(length=1000), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dog")
    # ### end Alembic commands ###
