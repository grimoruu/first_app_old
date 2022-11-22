from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship
# from users.models import Users

user_board_association = Table(
    'users_boards', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('board_id', Integer, ForeignKey('boards.id'))
)

class Board(Base):
    __tablename__ = 'boards'
    
    id = Column(Integer, primary_key=True, unique = True)
    title = Column(String(20), nullable=False)
    date_created = Column(DateTime)
    users = relationship('User', secondary=user_board_association)

    def __init__(self, title, date_created):
        self.title = title
        self.date_created = date_created