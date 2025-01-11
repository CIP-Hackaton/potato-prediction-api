from fastapi import APIRouter, Depends, Request, HTTPException
from dependency_injector.wiring import inject, Provide

from app.container import Container
from app.services.predict_service import PredictService
from app.schemas.predictions import FormPredict
from app.utils.date_to_month import date_to_month

router = APIRouter()

@router.post("")
@inject
def predict(request: Request, form: FormPredict, predict_service: PredictService = Depends(Provide[Container.predict_service])):
    try: 
        form.date = date_to_month(form.date)
        user_id = request.state.user_id

        new_prediction = predict_service.predict(form, user_id)

        return new_prediction
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))