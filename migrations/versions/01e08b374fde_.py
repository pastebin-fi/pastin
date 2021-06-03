"""empty message

Revision ID: 01e08b374fde
Revises: bb9d77814d2e
Create Date: 2021-06-03 19:27:19.511853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e08b374fde'
down_revision = 'bb9d77814d2e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("paste", "content", type_=sa.Text(1048576))


def downgrade():
    op.alter_column("paste", "content", type_=sa.UnicodeText())
