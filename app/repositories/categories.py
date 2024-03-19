from abc import abstractmethod, ABC

from fastapi import Depends

from app.database.db import SessionLocal, get_db
from app.database.models.categories import Category as DBCategory, Category


class ICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Category]:
        pass

    @abstractmethod
    def get_by_id(self, category_id) -> Category:
        pass


class CategoryRepository(ICategoryRepository):
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_all(self) -> list[Category]:
        return self.db.query(DBCategory).all()

    def get_by_id(self, category_id) -> Category:
        return self.db.get(DBCategory, category_id)


def get_category_repository(db: SessionLocal = Depends(get_db)) -> CategoryRepository:
    return CategoryRepository(db)
