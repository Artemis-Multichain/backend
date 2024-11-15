"""updated encryption models

Revision ID: 15436d808394
Revises: ce3ca30a6baa
Create Date: 2024-09-12 18:55:05.757860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15436d808394'
down_revision: Union[str, None] = 'ce3ca30a6baa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encrypted_keys', sa.Column('aes_encrypted_private_key', sa.String(), nullable=False))
    op.add_column('encrypted_keys', sa.Column('aes_key', sa.String(), nullable=False))
    op.drop_column('encrypted_keys', 'encrypted_private_key')
    op.drop_column('encrypted_keys', 'public_key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encrypted_keys', sa.Column('public_key', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('encrypted_keys', sa.Column('encrypted_private_key', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('encrypted_keys', 'aes_key')
    op.drop_column('encrypted_keys', 'aes_encrypted_private_key')
    # ### end Alembic commands ###
