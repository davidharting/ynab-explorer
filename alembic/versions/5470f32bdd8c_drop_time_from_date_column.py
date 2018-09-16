"""drop time from date column

Revision ID: 5470f32bdd8c
Revises: 355407ede2e6
Create Date: 2018-09-16 12:39:35.044605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5470f32bdd8c'
down_revision = '355407ede2e6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('transactions', 'date', type_ = sa.Date)


def downgrade():
    op.alter_column('transactions', 'date', type_ = sa.DateTime)
