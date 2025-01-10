from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.schemas.auth import UserCreateSchema, UserSchema, UserLoginSchema
from app.services.potatoes_service import PotatoesService

router = APIRouter()

@router.get("")
@inject
def register_user(potatoes_service: PotatoesService = Depends(Provide[Container.potatoes_service])):
    return potatoes_service.get_potatoes()

@router.get("/{potato_id}")
@inject
def get_potato(potato_id: int, potatoes_service: PotatoesService = Depends(Provide[Container.potatoes_service])):
    try:
        return potatoes_service.get_potato(potato_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Potato not found")
    
@router.get("/{potato_id}/characteristics")
@inject
def get_characteristics(potato_id: int, potatoes_service: PotatoesService = Depends(Provide[Container.potatoes_service])):
    try:
        return potatoes_service.get_characteristics(potato_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Potato not found")