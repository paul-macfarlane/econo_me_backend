from uuid import UUID

from fastapi import Depends

from app.models.categories import Category
from app.models.errors import ModelNotFoundException
from app.repositories.categories import ICategoryRepository, CategoryRepository, get_category_repository


class CategoryService:
    def __init__(self, category_repo: ICategoryRepository):
        self.category_repo = category_repo

    def get_all(self) -> list[Category]:
        return self.category_repo.get_all()

    def get_by_id(self, category_id: UUID) -> Category:
        category = self.category_repo.get_by_id(category_id)
        if not category:
            raise ModelNotFoundException("Category", str(category_id))

        return category


def get_category_service(category_repo: CategoryRepository = Depends(get_category_repository)) -> CategoryService:
    return CategoryService(category_repo)
