from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CreateTransaction(BaseModel):
    amount: float
    date: str
    categoryId: str
    userId: str  # this should eventually come from jwt
    description: str


class UpdateTransaction(BaseModel):
    amount: float | None
    date: str | None
    categoryId: str | None
    userId: str | None  # this should eventually come from jwt
    description: str | None


class TransactionResponse(BaseModel):
    id: str
    amount: float
    date: str
    categoryId: str
    userId: str
    description: str
    createdAt: str
    modifiedAt: str


@router.get("", response_model=list[TransactionResponse])
def list_transactions():
    return [{
        "id": "1",
        "amount": 100.0,
        "date": "2021-01-01",
        "categoryId": "1",
        "userId": "1",
        "description": "test",
        "createdAt": "2021-01-01",
        "modifiedAt": "2021-01-01"
    }]


@router.post("", response_model=TransactionResponse)
def create_transaction(transaction: CreateTransaction):
    return {
        "id": "1",
        "amount": transaction.amount,
        "date": transaction.date,
        "categoryId": transaction.categoryId,
        "userId": transaction.userId,
        "description": transaction.description,
        "createdAt": "2021-01-01",
        "modifiedAt": "2021-01-01"
    }


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: str):
    return {
        "id": transaction_id,
        "amount": 100.0,
        "date": "2021-01-01",
        "categoryId": "1",
        "userId": "1",
        "description": "test",
        "createdAt": "2021-01-01",
        "modifiedAt": "2021-01-01"
    }


@router.patch("/{transaction_id}", response_model=TransactionResponse)
def update_transaction(transaction_id: str, transaction: UpdateTransaction):
    # in a real implementation only the non-null fields would get set
    return {
        "id": transaction_id,
        "amount": transaction.amount,
        "date": transaction.date,
        "categoryId": transaction.categoryId,
        "userId": transaction.userId,
        "description": transaction.description,
        "createdAt": "2021-01-01",
        "modifiedAt": "2021-01-01"
    }


@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: str):
    return None
