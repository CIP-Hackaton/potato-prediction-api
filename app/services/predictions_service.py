from app.repositories.predictions_repository import PredictionsRepository
from app.models.predictions import Predictions

from app.services.user_service import UserService

class PredictionsService:
    def __init__(self, predictions_repository: PredictionsRepository, user_service: UserService):
        self.predictions_repository = predictions_repository
        self.user_service = user_service
    
    def get_predictions(self, user_id: str):
        try:
            predictions = self.predictions_repository.get_predictions(user_id)
            
            filtered_response = [
                {
                    'id': prediction.id,
                    'name': prediction.details['name'],
                    'date': prediction.created_at.strftime('%Y-%m-%d')
                }
                for prediction in predictions
            ]
            
            return filtered_response
        except Exception as e:
            raise Exception(f"Error getting predictions for user {user_id}")

    def get_prediction(self, prediction_id):
        try:
            prediction = self.predictions_repository.get_prediction(prediction_id)
            return prediction
        except Exception as e:
            raise Exception(f"Error getting prediction {prediction_id}")
    
    def create_prediction(self, prediction):
        try:
            new_prediction = Predictions(**prediction)
            return self.predictions_repository.create_prediction(new_prediction)
        except Exception as e:
            raise Exception(f"Error creating prediction")
    
    def add_user(self, prediction_id, new_user_email):
        try:
            
            # Let's verufy if the user exists
            new_user = self.user_service.get_user_by_email(new_user_email)

            if not new_user:
                raise ValueError("User not found")
            
            updated_prediction = self.predictions_repository.get_prediction(prediction_id)

            if not updated_prediction:
                raise ValueError("Prediction not found")

            allowed_user = updated_prediction.allowed_user
            updated_prediction.allowed_user = allowed_user.concat(new_user_email)
            return self.predictions_repository.update_prediction(prediction_id, updated_prediction)
        except Exception as e:
            raise Exception(f"Error updating prediction {prediction_id}")