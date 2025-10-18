"""create user table

Revision ID: a08fc6d1cdd8
Revises: a618ca0f1f09
Create Date: 2025-10-18 09:22:27.698348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a08fc6d1cdd8'
down_revision: Union[str, Sequence[str], None] = 'a618ca0f1f09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass
"""create user table"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'create_user_table'  
down_revision = 'a618ca0f1f09'  # replace with your last migration ID
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True, index=True),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True, index=True),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
    )


def downgrade() -> None:
    op.drop_table('users')


def downgrade() -> None:
    """Downgrade schema."""
    pass
