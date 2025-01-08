from app.models.role import Role
from app.models.user import User
from app.models.predictions import Predictions
from app.models.potatoes import Potatoes

# Esto asegura que todas las relaciones estén disponibles
__all__ = ['Role', 'User', 'Predictions', 'Potatoes']
