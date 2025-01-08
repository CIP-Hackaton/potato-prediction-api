from app.repositories.potatoes_repository import PotatoesRepository

class PotatoesService:

    def __init__(self, potatoes_repository: PotatoesRepository):
        self.potatoes_repository = potatoes_repository

    def get_potatoes(self):
        try:
            potatoes = self.potatoes_repository.get_potatoes()
            return potatoes
        except Exception as e:
            raise Exception(f"Error getting potatoes")
        
    def get_potato(self, potato_id):
        try:
            potato = self.potatoes_repository.get_potato(potato_id)
            return potato
        except Exception as e:
            raise Exception(f"Error getting potato {potato_id}")
    
    def get_characteristics(self, potato_id):
        try:
            characteristics = self.potatoes_repository.get_potato(potato_id).characteristics
            return characteristics
        except Exception as e:
            raise Exception(f"Error getting characteristics for potato {potato_id}")