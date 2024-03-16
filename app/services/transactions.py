from fastapi import Depends
from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.repositories.transactions import ITransactionRepository, TransactionRepository, get_transaction_repository
from uuid import UUID


class TransactionService:
    def __init__(self, transaction_repo: ITransactionRepository = Depends()):
        self.transaction_repo = transaction_repo

    def list(self, user_id: UUID) -> list[Transaction]:
        return self.transaction_repo.list(user_id)

    def get_by_id(self, user_id: UUID, transaction_id: UUID) -> Transaction:
        # TODO handle case where transaction is not found
        return self.transaction_repo.get_by_id(user_id, transaction_id)

    def create(self, user_id: UUID, create: CreateTransaction) -> Transaction:
        return self.transaction_repo.create(user_id, create)

    def update(self, user_id: UUID, transaction_id: UUID, update: UpdateTransaction) -> Transaction:
        # TODO handle case where transaction is not found
        return self.transaction_repo.update(user_id, transaction_id, update)

    def delete(self, user_id: UUID, transaction_id: UUID) -> None:
        # TODO handle case where transaction is not found
        return self.transaction_repo.delete(user_id, transaction_id)


def get_transaction_service(
        transaction_repo: TransactionRepository = Depends(get_transaction_repository)) -> TransactionService:
    return TransactionService(transaction_repo)
