from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: UUID
    email: EmailStr
    createdAt: datetime
    updatedAt: datetime


class CreateUser(BaseModel):
    email: EmailStr
    hashedPassword: str
