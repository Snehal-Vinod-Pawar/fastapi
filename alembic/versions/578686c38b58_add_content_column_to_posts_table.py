""" add content column to posts table

Revision ID: 578686c38b58
Revises: b27d646cd47a
Create Date: 2026-04-21 19:38:14.789485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '578686c38b58'
down_revision: Union[str, Sequence[str], None] = 'b27d646cd47a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
