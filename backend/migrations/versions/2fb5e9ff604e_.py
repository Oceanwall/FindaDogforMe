"""empty message

Revision ID: 2fb5e9ff604e
Revises: b34d4763c087
Create Date: 2019-03-20 12:13:07.829266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2fb5e9ff604e"
down_revision = "b34d4763c087"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "dog", "breed", existing_type=sa.VARCHAR(length=255), nullable=False
    )
    op.alter_column(
        "dog", "shelter_id", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.create_foreign_key(None, "dog", "shelter", ["shelter_id"], ["id"])
    op.create_foreign_key(None, "dog", "breed", ["breed"], ["name"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "dog", type_="foreignkey")
    op.drop_constraint(None, "dog", type_="foreignkey")
    op.alter_column(
        "dog", "shelter_id", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column("dog", "breed", existing_type=sa.VARCHAR(length=255), nullable=True)
    # ### end Alembic commands ###
