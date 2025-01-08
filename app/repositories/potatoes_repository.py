from sqlalchemy.orm import Session
from typing import Callable
from contextlib import AbstractContextManager

from app.models.potatoes import Potatoes

class PotatoesRepository():   

    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    def get_potatoes(self):
        with self.db() as session:
            return session.query(Potatoes).all()

    def get_potato(self, potato_id):
        with self.db() as session:
            return session.query(Potatoes).filter(Potatoes.id == potato_id).first()
        
