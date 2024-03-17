from fastapi import Depends

from app.models.errors import ModelNotFoundError
from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.repositories.transactions import ITransactionRepository, TransactionRepository, get_transaction_repository
from uuid import UUID


class TransactionService:
    def __init__(self, transaction_repo: ITransactionRepository = Depends()):
        self.transaction_repo = transaction_repo

    def list(self, user_id: UUID) -> list[Transaction]:
        return self.transaction_repo.list(user_id)

    def get_by_id(self, user_id: UUID, transaction_id: UUID) -> Transaction:
        transaction = self.transaction_repo.get_by_id(user_id, transaction_id)
        if not transaction:
            raise ModelNotFoundError("Transaction", str(transaction_id))

        return transaction

    def create(self, user_id: UUID, create: CreateTransaction) -> Transaction:
        return self.transaction_repo.create(user_id, create)

    def update(self, user_id: UUID, transaction_id: UUID, update: UpdateTransaction) -> Transaction:
        # note update already checks if the transaction exists and raises an error if it doesn't
        
        return self.transaction_repo.update(user_id, transaction_id, update)

    def delete(self, user_id: UUID, transaction_id: UUID) -> None:
        existing_transaction = self.get_by_id(user_id, transaction_id)
        if not existing_transaction:
            raise ModelNotFoundError("Transaction", str(transaction_id))

        return self.transaction_repo.delete(user_id, transaction_id)


def get_transaction_service(
        transaction_repo: TransactionRepository = Depends(get_transaction_repository)) -> TransactionService:
    return TransactionService(transaction_repo)
