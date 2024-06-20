"""added tag

Revision ID: 9898885fd8aa
Revises: 1315ced76ce6
Create Date: 2024-06-13 21:09:40.259680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9898885fd8aa'
down_revision: Union[str, None] = '1315ced76ce6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('tag', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'tag')
    # ### end Alembic commands ###