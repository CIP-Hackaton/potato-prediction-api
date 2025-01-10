from app.repositories.potatoes_repository import PotatoesRepository

class PotatoesService:

    def __init__(self, potatoes_repository: PotatoesRepository):
        self.potatoes_repository = potatoes_repository
    
    ordinal_mapping = {
        'Tizón tardío': {0: 'Altamente Suceptible', 1: 'Suceptible', 2: 'Moderadamente resistente', 3: 'Resistente'},
        'Periodo de crecimiento en altura': {0: 'Temprana', 1: 'Media', 2: 'Tardía'}
    }

    def get_potatoes(self):
        try:
            potatoes = self.potatoes_repository.get_potatoes()

            for potato in potatoes:

                if potato.characteristics['Color amarillo pálido predominante de la pulpa'] == 1:
                    potato.characteristics['Color predominante de la pulpa'] = "Amarillo"
                    potato.characteristics.pop('Color crema predominante de la pulpa')
                    potato.characteristics.pop('Color amarillo pálido predominante de la pulpa')
                else:  
                    potato.characteristics['Color predominante de la pulpa'] = "Crema"
                    potato.characteristics.pop('Color crema predominante de la pulpa')
                    potato.characteristics.pop('Color amarillo pálido predominante de la pulpa')

                if potato.characteristics['Forma: Ojos poco profundos'] == 1:
                    potato.characteristics['Forma de los ojos'] = "Poco profundos"
                    potato.characteristics.pop('Forma: Ojos poco profundos')
                    potato.characteristics.pop('Forma: Ojos ligeramente profundos')
                else:
                    potato.characteristics['Forma de los ojos'] = "Ligeramente profundos"
                    potato.characteristics.pop('Forma: Ojos poco profundos')
                    potato.characteristics.pop('Forma: Ojos ligeramente profundos')    

                for key, mapping in self.ordinal_mapping.items():
                    if key in potato.characteristics:
                        potato.characteristics[key] = mapping[potato.characteristics[key]] 
     

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