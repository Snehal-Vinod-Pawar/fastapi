"""create post table

Revision ID: b27d646cd47a
Revises: 
Create Date: 2026-04-21 19:21:54.371883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b27d646cd47a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass