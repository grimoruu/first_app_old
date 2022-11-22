from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship

class List(Base):
    __tablename__ = 'lists'
    
    id = Column(Integer, primary_key=True, unique = True)
    title = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    date_created = Column(DateTime)
    board = relationship('Board', backref='lists')
    board_id = Column(Integer, ForeignKey('boards.id'))
    
    def __init__(self, title, description, date_created):
        self.title = title
        self.description = description
        self.date_created = date_created

