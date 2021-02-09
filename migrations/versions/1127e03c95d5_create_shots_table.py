"""create shots table

Revision ID: 1127e03c95d5
Revises: 89ee0813931e
Create Date: 2021-02-05 18:42:13.763071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1127e03c95d5'
down_revision = '89ee0813931e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('players',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=255), nullable=True),
                    sa.Column('full_name', sa.String(
                        length=255), nullable=True),
                    sa.Column('last_name', sa.String(
                        length=255), nullable=True),
                    sa.Column('nba_player_id', sa.Integer(),
                              nullable=True, unique=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('shots',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('nba_player_id', sa.Integer(), nullable=True),
                    sa.Column('x', sa.Integer(), nullable=True),
                    sa.Column('y', sa.Integer(), nullable=True),
                    sa.Column('shot_zone', sa.String(
                        length=255), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['nba_player_id'], ['players.nba_player_id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('shots')