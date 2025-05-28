from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from exceptions.exception import token_exception
from config.config import Config
from model.auth_response import AuthResponse
from model.user import User
from model.user_response import UserResponse
from service import user_service

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
config = Config()

async def authenticate_user(username: str, password: str) -> Optional[User]:
    user = await user_service.get_user_by_username(username)
    if not user or not user_service.varify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(username: str, user_id: int) -> AuthResponse:
    user_date = {"subject": username, "id": user_id}
    token_expire = datetime.utcnow() + timedelta(minutes=config.TOKEN_EXPIRY_TIME)
    user_date.update({"exp": token_expire})
    token = jwt.encode(user_date, config.SECRET_KEY, config.ALGORITHM)
    return AuthResponse(jwt_token=token)


async def validate_user(token: str = Depends(oauth2_bearer)):
    return await validate_user_check(token)


async def validate_user_check(token: str) -> Optional[UserResponse]:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username = payload.get("subject")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise token_exception()
        else:
            return await user_service.get_user_by_id(user_id)
    except JWTError:
        raise token_exception()
