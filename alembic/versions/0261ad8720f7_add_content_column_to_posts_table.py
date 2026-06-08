"""Add content column to posts table

Revision ID: 0261ad8720f7
Revises: 087f46917548
Create Date: 2026-06-08 10:49:54.427907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0261ad8720f7'
down_revision: Union[str, Sequence[str], None] = '087f46917548'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
