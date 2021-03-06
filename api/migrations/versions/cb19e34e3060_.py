"""empty message

Revision ID: cb19e34e3060
Revises: d14c367218c2
Create Date: 2018-11-29 16:41:55.376419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb19e34e3060'
down_revision = 'd14c367218c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('examtype',
    sa.Column('exam_type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('exam_type_name', sa.String(length=25), nullable=False),
    sa.Column('exam_color', sa.String(length=10), nullable=False),
    sa.Column('number_of_hours', sa.Integer(), nullable=False),
    sa.Column('method_type', sa.String(length=10), nullable=False),
    sa.Column('ita_ind', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('exam_type_id')
    )
    op.create_table('invigilator',
    sa.Column('invigilator_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('invigilator_name', sa.String(length=50), nullable=False),
    sa.Column('invigilator_notes', sa.String(length=400), nullable=True),
    sa.Column('contact_phone', sa.String(length=15), nullable=True),
    sa.Column('contact_email', sa.String(length=50), nullable=True),
    sa.Column('contract_number', sa.String(length=50), nullable=False),
    sa.Column('contract_expiry_date', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ),
    sa.PrimaryKeyConstraint('invigilator_id')
    )
    op.create_table('room',
    sa.Column('room_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('room_name', sa.String(length=50), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=25), nullable=False),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ),
    sa.PrimaryKeyConstraint('room_id')
    )
    op.create_table('booking',
    sa.Column('booking_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('fees', sa.String(length=5), nullable=True),
    sa.Column('booking_name', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.PrimaryKeyConstraint('booking_id')
    )
    op.create_table('exam',
    sa.Column('exam_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('booking_id', sa.Integer(), nullable=True),
    sa.Column('exam_type_id', sa.Integer(), nullable=False),
    sa.Column('invigilator_id', sa.Integer(), nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.String(length=25), nullable=False),
    sa.Column('exam_name', sa.String(length=50), nullable=False),
    sa.Column('examinee_name', sa.String(length=50), nullable=False),
    sa.Column('expiry_date', sa.DateTime(), nullable=False),
    sa.Column('notes', sa.String(length=400), nullable=True),
    sa.Column('exam_received', sa.Integer(), nullable=False),
    sa.Column('session_number', sa.Integer(), nullable=False),
    sa.Column('number_of_students', sa.Integer(), nullable=False),
    sa.Column('exam_method', sa.String(length=15), nullable=False),
    sa.Column('deleted_date', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['booking.booking_id'], ),
    sa.ForeignKeyConstraint(['exam_type_id'], ['examtype.exam_type_id'], ),
    sa.ForeignKeyConstraint(['invigilator_id'], ['invigilator.invigilator_id'], ),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.PrimaryKeyConstraint('exam_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exam')
    op.drop_table('booking')
    op.drop_table('room')
    op.drop_table('invigilator')
    op.drop_table('examtype')
    # ### end Alembic commands ###
