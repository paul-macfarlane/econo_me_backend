from fastapi import Depends
from abc import ABC, abstractmethod

from app.database.db import SessionLocal, get_db
from app.models.users import User, CreateUser
from app.database.models.users import User as DBUser
from pydantic import EmailStr


class IUserRepository(ABC):
    @abstractmethod
    def get_by_email_include_password(self, email: EmailStr) -> DBUser | None:
        pass

    @abstractmethod
    def get_by_email(self, email: EmailStr) -> User | None:
        pass

    @abstractmethod
    def create(self, create: CreateUser) -> User:
        pass


class UserRepository(IUserRepository):
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_by_email_include_password(self, email: EmailStr) -> DBUser | None:
        return self.db.query(DBUser).filter(DBUser.email == email).first()

    def get_by_email(self, email: EmailStr) -> User | None:
        return self.db.query(DBUser).filter(DBUser.email == email).first()

    def create(self, create: CreateUser) -> User:
        new_user = DBUser(email=create.email, hashedPassword=create.hashedPassword)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return User(id=new_user.id, email=new_user.email, createdAt=new_user.createdAt, updatedAt=new_user.modifiedAt)


def get_user_repository(db: SessionLocal = Depends(get_db)) -> UserRepository:
    return UserRepository(db)
