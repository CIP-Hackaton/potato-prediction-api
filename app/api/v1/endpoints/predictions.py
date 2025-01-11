from fastapi import APIRouter, Depends, HTTPException, status, Request
from dependency_injector.wiring import inject, Provide

from app.schemas.predictions import AddUserRequest
from app.container import Container
from app.services.predictions_service import PredictionsService 

router = APIRouter()

@router.get("")
@inject
def get_predictions(
    request: Request,
    predictions_service: PredictionsService = Depends(Provide[Container.predictions_service])
):
    user_id = request.state.user_id
    return predictions_service.get_predictions(user_id)

@router.get("/{prediction_id}")
@inject
def get_prediction(prediction_id: str, predictions_service: PredictionsService = Depends(Provide[Container.predictions_service])):
    try:
        return predictions_service.get_prediction(prediction_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found")


@router.put("/{prediction_id}")
@inject
def add_user(
    prediction_id: int, 
    request: AddUserRequest,
    predictions_service: PredictionsService = Depends(Provide[Container.predictions_service])
):
    try:
        return predictions_service.add_user(prediction_id, request.new_user_email)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found")