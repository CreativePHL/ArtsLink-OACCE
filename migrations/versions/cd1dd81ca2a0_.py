"""empty message

Revision ID: cd1dd81ca2a0
Revises: c11bb644732d
Create Date: 2018-04-07 16:53:44.585776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd1dd81ca2a0'
down_revision = 'c11bb644732d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_assocation')
    op.drop_column('tag_association', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag_association', sa.Column('id', sa.INTEGER(), nullable=False))
    op.create_table('tag_assocation',
    sa.Column('tag_id', sa.INTEGER(), nullable=True),
    sa.Column('organization_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###
