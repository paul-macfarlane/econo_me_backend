from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, field_validator, Field


class CreateTransaction(BaseModel):
    amount: float = Field(ge=0)
    date: str
    categoryId: UUID
    description: str = Field(min_length=1)

    # make sure
    @field_validator("date")
    def date_must_be_YYYY_MM_DD(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in the format YYYY-MM-DD")

        return value


class UpdateTransaction(BaseModel):
    amount: Optional[float] = None
    date: Optional[str] = None
    categoryId: Optional[UUID] = None
    description: Optional[str] = None

    @field_validator("amount")
    def amount_ge_0(cls, value):
        if value is not None and value < 0:
            raise ValueError("Amount must be greater than or equal to 0")

        return value

    @field_validator("date")
    def date_must_be_YYYY_MM_DD(cls, value):
        if value is not None:
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in the format YYYY-MM-DD")

        return value

    @field_validator("description")
    def description_must_have_at_least_1_character(cls, value):
        if value is not None and len(value) < 1:
            raise ValueError("Description must have at least 1 character")

        return value


class Transaction(BaseModel):
    id: UUID
    amount: float
    date: str
    categoryId: UUID
    userId: UUID
    description: str
    createdAt: datetime
    modifiedAt: datetime
