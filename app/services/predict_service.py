from fastapi import HTTPException
import uuid

from app.ai.model import Model
from app.services.predictions_service import PredictionsService
from app.schemas.predictions import FormPredict


class PredictService:

    ordinal_mapping = {
        'Tizón tardío': {0: 'Altamente Suceptible', 1: 'Suceptible', 2: 'Moderadamente resistente', 3: 'Resistente'},
        'Periodo de crecimiento en altura': {0: 'Temprana', 1: 'Media', 2: 'Tardía'}
    }

    def __init__(self, model: Model, predictions_service: PredictionsService):
        self.model = model
        self.predictions_service = predictions_service

    
    def post_process(self, form: FormPredict, norma_variedades: list, vector_ideal: list, user_id):
        
        if form.mode == "automatic":
            details = {
                "name": form.name,
                "Fecha": form.date,
                "Departamento": form.department,
                "Provincia": form.province,
                "Distrito": form.district,
                "mode": "automatic"
            }
        
        
        color_pulpa = "Amarillo" if vector_ideal[0][3] == 1 else "Crema"
        forma_ojos = "Poco profundos" if vector_ideal[0][4] == 1 else "Ligeramente profundos"

        p_characteristics = { 
            "Tizón tardío": self.ordinal_mapping['Tizón tardío'][vector_ideal[0][0]],
            "Materia Seca": float(vector_ideal[0][1]),
            "Periodo de crecimiento en altura": self.ordinal_mapping['Periodo de crecimiento en altura'][vector_ideal[0][2]],
            "Color predominante de la pulpa": color_pulpa,
            "Forma de los ojos": forma_ojos
        }

        normvariedades_dict = {f"variedad_{i}": variedad for i, variedad in enumerate(norma_variedades)}
   
        prediction ={
            "details": details,
            "owner": user_id,
            "p_characteristics": p_characteristics,
            "campesino_response": normvariedades_dict,
            "allowed_user": [user_id]
        }

        return prediction
        


    def predict(self, form: FormPredict, user_id):   

        norma_variedades = []
        vector_papa_ideal = [] 
        
        if form.mode == "automatic":
            norma_variedades, vector_papa_ideal = self.model.predict_automatic_mode(form.date, form.department, form.province, form.district)
        
        elif form.mode == "manual":
            """"
            data = {
                "mes": form.date,
                "departamento": form.department,
                "provincia": form.province,
                "distrito": form.district,
                "temp_max": form.temp_max,
                "temp_min": form.temp_min,
                "humedad": form.humidity,
                "precipitacion": form.rainfall,
                "clasi": form.clasi,
                "nevada": form.nevada,
                "erosion": form.erosion
            }
            norma_variedades, vector_papa_ideal = self.model.predict_manual_mode(data)
            """
            raise HTTPException(status_code=501, detail="Not implemented")
        else:
            raise HTTPException(status_code=501, detail="Not implemented")

        prediction = self.post_process(form, norma_variedades, vector_papa_ideal, user_id)
        
        try:
            prediction_response = self.predictions_service.create_prediction(prediction)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating prediction: {str(e)}")
        
        return prediction_response
