from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class AddUserRequest(BaseModel):
    new_user_email: str


class FormPredict(BaseModel):
    name: str
    date: str 
    mode: str
    department: Optional[str] = None
    province: Optional[str] = None
    district: Optional[str] = None
    temp_max: Optional[float] = Field(default=None, alias="temp_max")
    temp_min: Optional[float] = Field(default=None, alias="temp_min")
    humidity: Optional[int] = None
    rainfall: Optional[float] = None
    clasi: Optional[str] = None
    nevada: Optional[float] = None
    erosion: Optional[float] = None

