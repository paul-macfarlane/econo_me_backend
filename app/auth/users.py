from app.auth.token import verify_token, oauth2_scheme
from app.models.errors import UnauthenticatedErrorException
from fastapi import Depends

from app.models.users import User
from app.repositories.users import get_user_repository


def get_current_user(user_repo=Depends(get_user_repository), token=Depends(oauth2_scheme)) -> User:
    credentials_exception = UnauthenticatedErrorException()
    user_id = verify_token(token.credentials, credentials_exception)

    user = user_repo.get_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user
