from sqlalchemy import Column, String, Float, func, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import Base
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    amount = Column(Float, nullable=False)
    date = Column(String, nullable=False)
    categoryId = Column(UUID, ForeignKey("categories.id"), nullable=False, name="category_id")
    category = relationship("Category", back_populates="transactions")
    userId = Column(UUID, ForeignKey("users.id"), nullable=False, name="user_id")
    user = relationship("User", back_populates="transactions")
    description = Column(String, nullable=False)
    createdAt = Column("created_at", DateTime, server_default=func.now(), nullable=False)
    modifiedAt = Column("modified_at", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
