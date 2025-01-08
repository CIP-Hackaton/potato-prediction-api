from app.ai.model import Model
from app.services.predictions_service import PredictionsService

class PredictService:
    def __init__(self, model: Model, predictions_service: PredictionsService):
        self.model = model
        self.predictions_service = predictions_service

    
    def postprocess(self, model_response):
        # TODO implement the postprocessing logic
        return model_response
    
    def preprocess(self, data):
        # TODO implement the preprocessing logic
        return data    

    def predict(self, data):
        # TODO preprocess the data
        data = self.preprocess(data)
        model_response = self.model.predict(data)

        # TODO postprocess the model response
        model_response = self.postprocess(model_response)
        self.predictions_service.create_prediction(model_response)
        return "uwu"
