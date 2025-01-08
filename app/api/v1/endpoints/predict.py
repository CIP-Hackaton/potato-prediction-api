from fastapi import APIRouter, Depends, Request
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.services.predict_service import PredictService
from app.schemas.predictions import PredictRequest

router = APIRouter()

@router.post("/")
@inject
def predict(request: Request, request_values: PredictRequest, predict_service: PredictService = Depends(Provide[Container.predict_service])):
    predict_respone = predict_service.predict(request_values.model_dump())

    user_id = request.state.user_id

    return 