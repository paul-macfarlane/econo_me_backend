from fastapi import Depends
from app.database.db import SessionLocal, get_db
from app.database.models.transactions import Transaction as DBTransaction
from app.models.transactions import CreateTransaction, Transaction, UpdateTransaction
from abc import ABC, abstractmethod
from uuid import UUID


class ITransactionRepository(ABC):
    @abstractmethod
    def list(self, user_id: UUID) -> list[Transaction]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID, transaction_id: UUID) -> Transaction:
        pass

    @abstractmethod
    def create(self, user_id: UUID, create: CreateTransaction) -> Transaction:
        pass

    @abstractmethod
    def update(self, user_id: UUID, transaction_id: UUID, update: UpdateTransaction) -> Transaction:
        pass

    @abstractmethod
    def delete(self, user_id: UUID, transaction_id: UUID) -> None:
        pass


# TODO: Replace fake implementation with real implementation containing database logic
class TransactionRepository(ITransactionRepository):
    def __init__(self, db: SessionLocal):
        self.db = db

    def list(self, user_id: UUID) -> list[Transaction]:
        return self.db.query(DBTransaction).filter(DBTransaction.userId == user_id).all()

    def get_by_id(self, user_id: UUID, transaction_id: UUID) -> Transaction:
        # TODO handle case where transaction is not found
        return self.db.query(DBTransaction).filter(DBTransaction.userId == user_id,
                                                   DBTransaction.id == transaction_id).first()

    def create(self, user_id: UUID, create: CreateTransaction) -> Transaction:
        db_transaction = DBTransaction(
            amount=create.amount,
            date=create.date,
            categoryId=create.categoryId,
            userId=user_id,
            description=create.description
        )

        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)

        return db_transaction

    def update(self, user_id: UUID, transaction_id: UUID, update: UpdateTransaction) -> Transaction:
        # TODO handle case where transaction is not found
        db_transaction = self.get_by_id(user_id, transaction_id)

        db_transaction.amount = update.amount
        db_transaction.date = update.date
        db_transaction.categoryId = update.categoryId
        db_transaction.description = update.description

        self.db.commit()
        self.db.refresh(db_transaction)

        return db_transaction

    def delete(self, user_id: UUID, transaction_id: UUID) -> None:
        # TODO handle case where transaction is not found
        db_transaction = self.get_by_id(user_id, transaction_id)

        self.db.delete(db_transaction)
        self.db.commit()


def get_transaction_repository(db: SessionLocal = Depends(get_db)) -> TransactionRepository:
    return TransactionRepository(db)
