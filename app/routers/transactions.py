from fastapi import APIRouter, Depends

from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.services.transactions import get_transaction_service, TransactionService

from uuid import UUID

router = APIRouter()

# TODO replace with real user id
fake_user_id = UUID('3fa85f64-5717-4562-b3fc-2c963f66afa6')


@router.get("", response_model=list[Transaction])
def list_transactions(transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.list(fake_user_id)


@router.post("", response_model=Transaction, status_code=201)
def create_transaction(create: CreateTransaction,
                       transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.create(fake_user_id, create)


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: UUID, transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.get_by_id(fake_user_id, transaction_id)


@router.patch("/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: UUID, update: UpdateTransaction,
                       transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.update(fake_user_id, transaction_id, update)


@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: UUID,
                       transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.delete(fake_user_id, transaction_id)
