from pathlib import Path
from typing import List

from starlette import status
from model.user_request import UserRequest
from fastapi import APIRouter, Depends

from model.user_response import UserResponse
from service import auth_service
from service import user_service
from exceptions.exception import token_exception

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    await user_service.create_user(user_request)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_users(user: UserResponse = Depends(auth_service.validate_user)):
    if user is None:
        raise token_exception()
    return await user_service.get_users()
