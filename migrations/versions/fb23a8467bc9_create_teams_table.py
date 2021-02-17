"""create teams table

Revision ID: fb23a8467bc9
Revises: b86400cbadd7
Create Date: 2021-02-17 17:21:01.766898

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import PrimaryKeyConstraint


# revision identifiers, used by Alembic.
revision = 'fb23a8467bc9'
down_revision = 'b86400cbadd7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('teams',
                    sa.Column('id', sa.Integer(),
                              nullable=False),
                    sa.Column('team_id', sa.Integer(), nullable=False),
                    sa.Column('team_name', sa.String(
                        length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teams')