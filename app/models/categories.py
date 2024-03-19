from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Category(BaseModel):
    id: UUID
    name: str
    type: str
    createdAt: datetime
    modifiedAt: datetime
