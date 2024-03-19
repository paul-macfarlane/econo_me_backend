from fastapi import Depends

from app.models.errors import ModelNotFoundException
from app.models.transactions import Transaction, CreateTransaction, UpdateTransaction
from app.repositories.categories import ICategoryRepository, get_category_repository
from app.repositories.transactions import ITransactionRepository, TransactionRepository, get_transaction_repository
from uuid import UUID


class TransactionService:
    def __init__(
            self,
            transaction_repo: ITransactionRepository = Depends(),
            category_repo: ICategoryRepository = Depends(),
    ):
        self.transaction_repo = transaction_repo
        self.category_repo = category_repo

    def list(self, user_id: UUID) -> list[Transaction]:
        return self.transaction_repo.list(user_id)

    def get_by_id(self, user_id: UUID, transaction_id: UUID) -> Transaction:
        transaction = self.transaction_repo.get_by_id(user_id, transaction_id)
        if not transaction:
            raise ModelNotFoundException("Transaction", str(transaction_id))

        return transaction

    def create(self, user_id: UUID, create: CreateTransaction) -> Transaction:
        category = self.category_repo.get_by_id(create.categoryId)
        if not category:
            raise ModelNotFoundException("Category", str(create.categoryId))

        return self.transaction_repo.create(user_id, create)

    def update(self, user_id: UUID, transaction_id: UUID, update: UpdateTransaction) -> Transaction:
        # note update already checks if the transaction exists and raises an error if it doesn't

        if update.categoryId is not None:
            category = self.category_repo.get_by_id(update.categoryId)
            if not category:
                raise ModelNotFoundException("Category", str(update.categoryId))

        return self.transaction_repo.update(user_id, transaction_id, update)

    def delete(self, user_id: UUID, transaction_id: UUID) -> None:
        existing_transaction = self.get_by_id(user_id, transaction_id)
        if not existing_transaction:
            raise ModelNotFoundException("Transaction", str(transaction_id))

        return self.transaction_repo.delete(user_id, transaction_id)


def get_transaction_service(
        transaction_repo: TransactionRepository = Depends(get_transaction_repository),
        category_repo: ICategoryRepository = Depends(get_category_repository),
) -> TransactionService:
    return TransactionService(transaction_repo, category_repo)
