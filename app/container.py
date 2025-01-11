from dependency_injector import containers, providers

from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.repositories.potatoes_repository import PotatoesRepository
from app.repositories.predictions_repository import PredictionsRepository
from app.services.auth_service import AuthService
from app.services.jwt_service import TokenServiceJWT
from app.services.potatoes_service import PotatoesService
from app.services.predict_service import PredictService
from app.services.predictions_service import PredictionsService
from app.services.user_service import UserService
from app.ai.model import Model
from app.config import settings

DATABASE_URL = settings.DATABASE_URL
JWT_SECRET_KEY = settings.JWT_SECRET_KEY

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.auth",
            "app.api.v1.endpoints.potatoes",
            "app.api.v1.endpoints.predict",
            "app.api.v1.endpoints.predictions",
            "app.api.v1.endpoints.user",
        ]
    )

    # Database
    db = providers.Singleton(SessionLocal, db_url=DATABASE_URL)

    # Repositories
    user_repository = providers.Factory(
        UserRepository,
        db=db.provided.session,
    )

    potatoes_repository = providers.Factory(
        PotatoesRepository,
        db=db.provided.session,
    )

    predictions_repository = providers.Factory(
        PredictionsRepository,
        db=db.provided.session,
    )

    # AI Model
    ai_model = providers.Singleton(Model)

    # Services
    jwt_service = providers.Factory(
        TokenServiceJWT,
        secret_key=JWT_SECRET_KEY       
    )

    auth_service = providers.Factory(
        AuthService,
        user_repository=user_repository,
        token_service=jwt_service
    )

    potatoes_service = providers.Factory(
        PotatoesService,
        potatoes_repository=potatoes_repository
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )


    predictions_service = providers.Factory(
        PredictionsService,
        predictions_repository=predictions_repository,
        user_service=user_service
    )

    predict_service = providers.Factory(
        PredictService,
        predictions_service=predictions_service,
        potatoes_service=potatoes_service,
        model=ai_model
    )
