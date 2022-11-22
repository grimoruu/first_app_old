from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship



class Board(Base):
    __tablename__ = 'boards'
    
    id = Column(Integer, primary_key=True, unique = True)
    title = Column(String(20), nullable=False)
    date_created = Column(DateTime)
    lists = relationship('List')
    
    def __init__(self, title, date_created):
        self.title = title
        self.date_created = date_created