from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship

list_task_association = Table(
    'lists_tasks', Base.metadata,
    Column('list_id', Integer, ForeignKey('lists.id')),
    Column('task_id', Integer, ForeignKey('tasks.id'))
)

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, unique = True)
    title = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    date_created = Column(DateTime)
    lists = relationship('List', secondary=list_task_association)
    
    def __init__(self, title, description, date_created):
        self.title = title
        self.description = description
        self.date_created = date_created
