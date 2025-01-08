from sqlalchemy.orm import Session
from typing import Callable, Optional
from contextlib import AbstractContextManager

from app.models.user import User

class UserRepository:   

    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    def get_by_id(self, user_id: str) -> User:
        with self.db() as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        with self.db() as session:
            return session.query(User).filter(User.email == email).first()

    def create_user(self, user: User) -> User:
        with self.db() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user
