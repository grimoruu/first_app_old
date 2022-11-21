from sqlalchemy import Column, String, Integer, DateTime, Index, Boolean, ForeignKey
from core.db import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique = True)
    username = Column(String(15), nullable=False, unique = True)
    password = Column(String(10), nullable=False)
    email = Column(String, nullable=False, unique = True)
    date_joined = Column(DateTime)
    is_active = Column(Boolean, default=False)
    board = Column(Integer, ForeignKey('board.id'))
    board_id = relationship('Board')