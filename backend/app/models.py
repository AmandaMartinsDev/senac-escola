from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = 'users'

    user_email = Column(String, primary_key=True, index=True)
    user_password = Column(String, unique=True, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    user_type = Column(String, unique=True, nullable=False)
    document_id = Column(Integer, unique=True, nullable=False)
    user_address = Column(String, unique=True, nullable=False)
    user_phone = Column(Integer, unique=True, nullable=False)
