from fastapi import Depends

from app.auth.hash import get_password_hash, verify_password
from app.auth.token import create_access_token
from app.models.auth import Token, SignUp, Login
from app.models.errors import UnauthenticatedErrorException, ResourceAlreadyExistsException, UserAlreadyExistsException
from app.models.users import CreateUser
from app.repositories.users import IUserRepository, UserRepository, get_user_repository


class AuthService:
    def __init__(self, user_repo: IUserRepository = Depends()):
        self.user_repo = user_repo

    def login(self, login: Login) -> Token:
        user = self.user_repo.get_by_email_include_password(login.email)
        if not user or not verify_password(login.password, user.hashedPassword):
            raise UnauthenticatedErrorException()

        return create_access_token(user.id)

    def sign_up(self, sign_up: SignUp) -> Token:
        existing_user = self.user_repo.get_by_email(sign_up.email)
        if existing_user:
            raise UserAlreadyExistsException(sign_up.email)

        new_user = self.user_repo.create(
            CreateUser(email=sign_up.email, hashedPassword=get_password_hash(sign_up.password)))

        return create_access_token(new_user.id)


def get_auth_service(user_repo: UserRepository = Depends(get_user_repository)):
    return AuthService(user_repo)
