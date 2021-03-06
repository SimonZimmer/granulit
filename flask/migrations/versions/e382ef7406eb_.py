"""empty message

Revision ID: e382ef7406eb
Revises: 2a744cd622d0
Create Date: 2021-02-27 14:25:25.635519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e382ef7406eb'
down_revision = '2a744cd622d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('impressum', sa.String(length=500000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.drop_column('impressum')

    # ### end Alembic commands ###
