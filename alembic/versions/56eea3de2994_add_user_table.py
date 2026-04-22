"""add user table

Revision ID: 56eea3de2994
Revises: 578686c38b58
Create Date: 2026-04-21 19:45:37.838767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56eea3de2994'
down_revision: Union[str, Sequence[str], None] = '578686c38b58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()'))
    )

def downgrade() -> None:
    op.drop_table('users')
    pass
