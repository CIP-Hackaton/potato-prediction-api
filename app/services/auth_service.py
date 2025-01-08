import bcrypt
import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreateSchema, UserLoginSchema
from app.config import settings

from app.services.jwt_service import TokenServiceJWT
from app.repositories.user_repository import UserRepository

SALT = bcrypt.gensalt(rounds=settings.SALT_ROUNDS)

class AuthService():

    def __init__(self, user_repository: UserRepository, token_service:TokenServiceJWT):
        self.user_repository = user_repository
        self.token_service = token_service

    def _hash_password(self, password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), SALT)
        return hashed_password.decode('utf-8')

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def register_user(self, user_data: UserCreateSchema) -> dict:
        try:
            hashed_password = self._hash_password(user_data.password)
            new_user = User(
                id=uuid.uuid4(),
                name=user_data.name,
                email=user_data.email,
                password=hashed_password,
                role=user_data.role,
            )

            created_user = self.user_repository.create_user(new_user)
            
            return { "message": "User created successfully" }
        except Exception as e:
            raise ValueError(f"Error creating user: {str(e)}")

    def authenticate_user(self, user_data: UserLoginSchema) -> str:
        user = self.user_repository.get_user_by_email(user_data.email)
        if not user:
            raise ValueError("Invalid credentials")

        if not bcrypt.checkpw(user_data.password.encode(), user.password.encode()):
            raise ValueError("Invalid credentials")

        # Include user_id in token payload
        token_data = {
            "user_id": str(user.id),
            "email": user.email
        }
        
        return self.token_service.create_token(token_data)
