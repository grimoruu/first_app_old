from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from core.db import Base
# from users.models import Users


class Board(Base):
    __tablename__ = 'board'
    
    id = Column(Integer, primary_key=True, unique = True)
    title = Column(String(20), nullable=False)
    date_created = Column(DateTime)
    
