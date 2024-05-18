from abc import ABC, abstractmethod

class Factory(ABC):
   
    _total = 0

    def __init__(self, model_name, fuel_type):
        self._model_name = model_name
        self._fuel_type = fuel_type
        Factory._total += 1
    
    
    @classmethod
    def get_total_created(cls):
        print(f"Total Vehicles : {cls._total}")

    @abstractmethod
    def get_model_name(self):
        pass
   
    @abstractmethod
    def get_fuel_type(self):
        pass
    
    @abstractmethod
    def set_model_name(self, value):
        pass
    
    @abstractmethod
    def set_fuel_type(self, value):
        pass

    @abstractmethod
    def get_number_of_wheels(self):
        pass