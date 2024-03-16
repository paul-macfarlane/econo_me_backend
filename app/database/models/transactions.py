from sqlalchemy import Column, String, Float, func
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import Base
import uuid


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = Column(Float)
    date = Column(String)
    categoryId = Column("category_id", UUID)  # TODO: Replace with foreign key to categories table
    userId = Column("user_id", UUID)  # TODO: Replace with foreign key to users table
    description = Column(String)
    createdAt = Column("created_at", String, server_default=func.now())
    modifiedAt = Column("modified_at", String, server_default=func.now(), onupdate=func.now())
