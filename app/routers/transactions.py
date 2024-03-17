from fastapi import APIRouter, Depends

from app.auth.token import oauth2_scheme
from app.auth.users import get_current_user
from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.models.users import User
from app.services.transactions import get_transaction_service, TransactionService

from uuid import UUID

router = APIRouter()


@router.get("", response_model=list[Transaction])
def list_transactions(
        transaction_service: TransactionService = Depends(get_transaction_service),
        current_user: User = Depends(get_current_user)
):
    return transaction_service.list(current_user.id)


@router.post("", response_model=Transaction, status_code=201)
def create_transaction(
        create: CreateTransaction,
        transaction_service: TransactionService = Depends(get_transaction_service),
        current_user: User = Depends(get_current_user)
):
    return transaction_service.create(current_user.id, create)


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(
        transaction_id: UUID,
        transaction_service:
        TransactionService = Depends(get_transaction_service),
        current_user: User = Depends(get_current_user)
):
    return transaction_service.get_by_id(current_user.id, transaction_id)


@router.patch("/{transaction_id}", response_model=Transaction)
def update_transaction(
        transaction_id: UUID,
        update: UpdateTransaction,
        transaction_service: TransactionService = Depends(get_transaction_service),
        current_user: User = Depends(get_current_user)
):
    return transaction_service.update(current_user.id, transaction_id, update)


@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(
        transaction_id: UUID,
        transaction_service: TransactionService = Depends(get_transaction_service),
        current_user: User = Depends(get_current_user)
):
    return transaction_service.delete(current_user.id, transaction_id)
