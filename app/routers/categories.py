from uuid import UUID

from fastapi import APIRouter, Depends

from app.auth.users import get_current_user
from app.models.categories import Category
from app.models.users import User
from app.services.categories import CategoryService, get_category_service

router = APIRouter()


@router.get("", response_model=list[Category])
def list_categories(
        category_service: CategoryService = Depends(get_category_service),
        current_user: User = Depends(get_current_user)
):
    return category_service.get_all()


@router.get("/{category_id}", response_model=Category)
def get_category(
        category_id: UUID,
        category_service: CategoryService = Depends(get_category_service),
        current_user: User = Depends(get_current_user)
):
    return category_service.get_by_id(category_id)
