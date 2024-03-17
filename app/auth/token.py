from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import UUID
from fastapi.security import HTTPBearer

from jose import JWTError, jwt

from app.models.auth import Token

# TODO These should be set as environment variables
SECRET_KEY = "a very secret key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = HTTPBearer()


def create_access_token(user_id: UUID, expires_delta: Optional[timedelta] = None) -> Token:
    to_encode = {"sub": str(user_id)}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return Token(accessToken=encoded_jwt, tokenType="bearer")


def verify_token(token: str, credentials_exception) -> UUID:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: UUID = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        return user_id
    except JWTError:
        raise credentials_exception
