from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.models.auth import Token, SignUp, Login
from app.services.auth import AuthService, get_auth_service

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/login", response_model=Token)
def login(login_req: Login, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login(login_req)


@router.post("/signup", response_model=Token)
def signup(sign_up: SignUp, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.sign_up(sign_up)
