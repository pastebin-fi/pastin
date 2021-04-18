"""empty message

Revision ID: bb9d77814d2e
Revises: 4e3b97e2f1d7
Create Date: 2021-04-18 23:28:19.527594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb9d77814d2e'
down_revision = '4e3b97e2f1d7'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("paste", "contents", existing_type=sa.UnicodeText(), new_column_name="content")


def downgrade():
    op.alter_column("paste", "content", existing_type=sa.UnicodeText(), new_column_name="contents")
