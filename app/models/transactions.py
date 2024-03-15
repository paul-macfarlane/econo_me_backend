from pydantic import BaseModel


class CreateTransaction(BaseModel):
    amount: float
    date: str
    categoryId: str
    description: str


class UpdateTransaction(BaseModel):
    amount: float | None
    date: str | None
    categoryId: str | None
    description: str | None


class Transaction(BaseModel):
    id: str
    amount: float
    date: str
    categoryId: str
    userId: str
    description: str
    createdAt: str
    modifiedAt: str
