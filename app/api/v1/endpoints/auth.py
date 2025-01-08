from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.schemas.auth import UserCreateSchema, UserSchema, UserLoginSchema
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
@inject
def register_user(user_data: UserCreateSchema, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    return auth_service.register_user(user_data)

@router.post("/login")
@inject
def login_user(user: UserLoginSchema, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    try:
        token = auth_service.authenticate_user(user)
        return { "access_token": token }
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
