from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, unique = True)
    username = Column(String(15), nullable=False, unique = True)
    password = Column(String(10), nullable=False)
    email = Column(String, nullable=False, unique = True)
    date_joined = Column(DateTime)
    is_active = Column(Boolean, default=False)
    
    def __init__(self, username, password, email, date_joined, is_active):
        self.username = username
        self.password = password
        self.email = email
        self.date_joined = date_joined
        self.is_active = is_active
