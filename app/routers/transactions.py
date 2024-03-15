from fastapi import APIRouter, Depends

from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.services.transactions import get_transaction_service, TransactionService

router = APIRouter()


@router.get("", response_model=list[Transaction])
def list_transactions(transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.list("1")  # TODO replace with real user id


@router.post("", response_model=Transaction, status_code=201)
def create_transaction(create: CreateTransaction,
                       transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.create("1", create)  # TODO replace with real user id


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: str, transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.get_by_id("1", transaction_id)  # TODO replace with real user id


@router.patch("/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: str, update: UpdateTransaction,
                       transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.update("1", transaction_id, update)  # TODO replace with real user id


@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: str, transaction_service: TransactionService = Depends(get_transaction_service)):
    return transaction_service.delete("1", transaction_id)  # TODO replace with real user id
