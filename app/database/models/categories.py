from sqlalchemy import Column, String, func, DateTime
from sqlalchemy.orm import relationship

from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Category(Base):
    __tablename__ = "categories"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    createdAt = Column(DateTime, nullable=False, name="created_at", server_default=func.now())
    modifiedAt = Column(DateTime, nullable=False, name="modified_at", server_default=func.now())

    transactions = relationship("Transaction", back_populates="category")
