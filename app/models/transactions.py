from uuid import UUID

from pydantic import BaseModel


class CreateTransaction(BaseModel):
    amount: float
    date: str
    categoryId: UUID
    description: str


class UpdateTransaction(BaseModel):
    amount: float | None
    date: str | None
    categoryId: UUID | None
    description: str | None


class Transaction(BaseModel):
    id: UUID
    amount: float
    date: str
    categoryId: UUID
    userId: UUID
    description: str
    createdAt: str
    modifiedAt: str
