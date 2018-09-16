"""create transactions table

Revision ID: 355407ede2e6
Revises: 
Create Date: 2018-07-29 10:46:44.584029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '355407ede2e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('date', sa.DateTime, nullable=False),
        sa.Column('amount', sa.Numeric, nullable=False),
        sa.Column('category', sa.String, nullable=False),
        sa.Column('payee', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('transactions')
