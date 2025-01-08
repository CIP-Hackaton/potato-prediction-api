from pydantic import BaseModel
from datetime import date

class AddUserRequest(BaseModel):
    new_user_email: str


class PredictRequest(BaseModel):
    fecha: date
    departamento: str
    provincia: str
    distrito: str
    nombre: str