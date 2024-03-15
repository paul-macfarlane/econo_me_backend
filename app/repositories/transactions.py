from app.models.transactions import CreateTransaction, Transaction, UpdateTransaction
from abc import ABC, abstractmethod


class ITransactionRepository(ABC):
    @abstractmethod
    def list(self, user_id: str) -> list[Transaction]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str, transaction_id: str) -> Transaction:
        pass

    @abstractmethod
    def create(self, user_id: str, create: CreateTransaction) -> Transaction:
        pass

    @abstractmethod
    def update(self, user_id: str, transaction_id: str, update: UpdateTransaction) -> Transaction:
        pass

    @abstractmethod
    def delete(self, user_id: str, transaction_id: str) -> None:
        pass


# TODO: Replace fake implementation with real implementation containing database logic
class TransactionRepository(ITransactionRepository):
    def __init__(self):
        pass

    def list(self, user_id: str) -> list[Transaction]:
        return [
            Transaction(
                id="1",
                amount=100.0,
                date="2021-01-01",
                categoryId="1",
                userId=user_id,
                description="test",
                createdAt="2021-01-01",
                modifiedAt="2021-01-01"
            )
        ]

    def get_by_id(self, user_id: str, transaction_id: str) -> Transaction:
        return Transaction(
            id=transaction_id,
            amount=100.0,
            date="2021-01-01",
            categoryId="1",
            userId=user_id,
            description="test",
            createdAt="2021-01-01",
            modifiedAt="2021-01-01"
        )

    def create(self, user_id: str, create: CreateTransaction) -> Transaction:
        return Transaction(
            id="1",
            amount=create.amount,
            date=create.date,
            categoryId=create.categoryId,
            userId=user_id,
            description=create.description,
            createdAt="2021-01-01",
            modifiedAt="2021-01-01"
        )

    def update(self, user_id: str, transaction_id: str, update: UpdateTransaction) -> Transaction:
        return Transaction(
            id=transaction_id,
            amount=update.amount,
            date=update.date,
            categoryId=update.categoryId,
            userId=user_id,
            description=update.description,
            createdAt="2021-01-01",
            modifiedAt="2021-01-01"
        )

    def delete(self, user_id: str, transaction_id: str) -> None:
        return None


def get_transaction_repository() -> TransactionRepository:
    return TransactionRepository()
