from vehicle_factory.factory import Factory

class Motorcycle(Factory):

    _total = 0

    def __init__(self, model_name, fuel_type, number_of_wheels = 2):
        super().__init__(model_name, fuel_type)
        self._number_of_wheels = number_of_wheels
        Motorcycle._total += 1

    
    def get_model_name(self):
        return self._model_name
   
    
    def get_fuel_type(self):
        return self._fuel_type
    
    
    def set_model_name(self, value):
        self._model_name = value
        return True
    
    def set_fuel_type(self, value):
        if value in ['electric', 'petrol', 'diesel']:
            self._fuel_type = value
            return True
        else:
            raise ValueError("Fuel type must be either 'electric', 'petrol', or 'diesel'")
        
    def get_number_of_wheels(self):
        return self._number_of_wheels

    @classmethod
    def get_total_created(cls):
        print(f"Total Motorcycles : {cls._total}")

    def __str__(self):
        return f"Model: {self.get_model_name()}, Fuel Type: {self.get_fuel_type()}, Number of Wheels: {self.get_number_of_wheels()}."
