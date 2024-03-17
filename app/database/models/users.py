from sqlalchemy import Column, String, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import Base
from sqlalchemy.orm import relationship
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashedPassword = Column(String, nullable=False, name="hashed_password")
    createdAt = Column(DateTime, server_default=func.now(), nullable=False, name="created_at")
    modifiedAt = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False, name="modified_at")

    transactions = relationship("Transaction", back_populates="user")
