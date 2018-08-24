"""empty message

Revision ID: 15162c60fa9f
Revises: 
Create Date: 2018-08-24 16:23:02.280288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15162c60fa9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Registered_User_Details',
    sa.Column('userid', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('userid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Registered_User_Details')
    # ### end Alembic commands ###