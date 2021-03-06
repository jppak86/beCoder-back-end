"""empty message

Revision ID: 80b2f455b7d5
Revises: edb1bf16974d
Create Date: 2022-04-13 19:30:02.240667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80b2f455b7d5'
down_revision = 'edb1bf16974d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('question', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'question')
    # ### end Alembic commands ###
