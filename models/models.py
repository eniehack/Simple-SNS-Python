from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
import ulid
from datetime import datetime


Base = declarative_base()


class User(Base):

    __tablename__ = "users"
    id = Column(String(15), primary_key=True, index=True)
    screen_name = Column(String(20))
    password = Column(String(150))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    is_admin = Column(Boolean, default=False)
    delete_flag = Column(Boolean, default=False)

    post = relationship("Post")
    relationship = relationship("Relationship")


class Post(Base):

    __tablename__ = "posts"
    id = Column(String(26), primary_key=True, default=ulid.new(), index=True)
    user_id = Column(String(15), ForeignKey("users.id"), index=True)
    body = Column(String(500))
    posted_at = Column(DateTime, default=datetime.now, index=True)
    delete_flag = Column(Boolean, default=False)


class Relationship(Base):

    __tablename__ = "relationship"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(15), ForeignKey("users.id"), index=True)
    target = Column(String(15), ForeignKey("users.id"), index=True)
    relationship = Column(Integer)
