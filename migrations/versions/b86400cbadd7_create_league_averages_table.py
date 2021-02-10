"""create league_averages table

Revision ID: b86400cbadd7
Revises: 1127e03c95d5
Create Date: 2021-02-09 19:06:53.196942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b86400cbadd7'
down_revision = '1127e03c95d5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('league_averages',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('shot_zone_basic', sa.String(
                        length=255), nullable=True),
                    sa.Column('shot_zone_area', sa.String(
                        length=255), nullable=True),
                    sa.Column('shot_zone_range', sa.String(
                        length=255), nullable=True),
                    sa.Column('fga', sa.Integer(), nullable=False),
                    sa.Column('fgm', sa.Integer(), nullable=False),
                    sa.Column('fg_pct', sa.Float(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('league_averages')
