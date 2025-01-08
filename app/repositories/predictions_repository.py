from sqlalchemy.orm import Session
from typing import Callable
from contextlib import AbstractContextManager

from app.models.predictions import Predictions

class PredictionsRepository():   

    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    def get_predictions(self, user_id: str) -> Predictions:
        with self.db() as session:
            return session.query(Predictions).filter(Predictions.owner == user_id).all()
        
    def get_prediction(self, prediction_id) -> Predictions:
        with self.db() as session:
            return session.query(Predictions).filter(Predictions.id == prediction_id).first()
        
    def create_prediction(self, prediction: Predictions) -> Predictions:
        with self.db() as session:
            session.add(prediction)
            session.commit()
            session.refresh(prediction)
            return prediction
    
    def update_prediction(self, prediction_id, prediction: Predictions):
        with self.db() as session:
            session.query(Predictions).filter(Predictions.id == prediction_id).update(prediction)
            session.commit()
            return prediction_id