from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.services.user_service import UserService

router = APIRouter()

@router.get("/me")
@inject
def register_user(user_service: UserService = Depends(Provide[Container.auth_service])):
    #TODO
    return "Hola"
