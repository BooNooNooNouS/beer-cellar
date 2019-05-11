"""initial beer and brewery tables

Revision ID: 897fb9d6221b
Revises: 
Create Date: 2019-05-11 16:14:32.226007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '897fb9d6221b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brewery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brewery_name'), 'brewery', ['name'], unique=True)
    op.create_table('beer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('style', sa.String(), nullable=True),
    sa.Column('brewery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brewery_id'], ['brewery.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_beer_name'), 'beer', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_beer_name'), table_name='beer')
    op.drop_table('beer')
    op.drop_index(op.f('ix_brewery_name'), table_name='brewery')
    op.drop_table('brewery')
    # ### end Alembic commands ###