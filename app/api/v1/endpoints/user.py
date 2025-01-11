from fastapi import APIRouter, Depends, Request, HTTPException
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.services.user_service import UserService

router = APIRouter()


role = {
    "1": "Campesino",
    "2": "Investigador"
}


@router.get("/me")
@inject
def register_user(request: Request, user_service: UserService = Depends(Provide[Container.user_service])):
    
    try:
        user_id = request.state.user_id
        user = user_service.get_user(user_id)
        user.created_at = user.created_at.strftime("%d-%m-%Y %H:%M:%S")

        user.role = role.get(str(user.role))

        user.password = "********"

        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/validate")
def validate_token():
    return {"message": "Token is valid"}