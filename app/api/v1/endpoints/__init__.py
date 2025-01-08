from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.potatoes import router as potatoes_router
from app.api.v1.endpoints.predict import router as predict_router
from app.api.v1.endpoints.predictions import router as predictions_router
from app.api.v1.endpoints.user import router as user_router
from app.api.v1.endpoints.health import router as health_router

router = APIRouter()


router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(potatoes_router, prefix="/potatoes", tags=["potatoes"])
router.include_router(predict_router, prefix="/predict", tags=["predict"])
router.include_router(predictions_router, prefix="/predictions", tags=["predictions"])
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(health_router, tags=["health"])

