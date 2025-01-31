"""Adding email to events and locations

Revision ID: c92daef11e16
Revises: 5ca7a52e90f0
Create Date: 2025-01-31 05:53:25.148655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c92daef11e16'
down_revision: Union[str, None] = '5ca7a52e90f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('email', sa.String(), nullable=True))
    op.add_column('locations', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locations', 'email')
    op.drop_column('events', 'email')
    # ### end Alembic commands ###
