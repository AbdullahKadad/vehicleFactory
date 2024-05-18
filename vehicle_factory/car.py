from vehicle_factory.factory import Factory

class Car(Factory):

    _total = 0

    def __init__(self, model_name,  fuel_type, number_of_doors, color, number_of_wheels = 4):
        super().__init__(model_name, fuel_type)
        self._number_of_wheels = number_of_wheels
        self._number_of_doors = number_of_doors
        self._color = color
        Car._total += 1

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

    def get_color(self):
        return self._color
    
    def set_color(self, value):
        self._color = value
        return True

    def get_number_of_doors(self):
        return self._number_of_doors
    
    def set_number_of_doors(self, value):
        if value in [2, 4]:
            self._number_of_doors = value
        else:
            raise ValueError("Number of doors must be either 2 or 4")
        
    def get_number_of_wheels(self):
        return self._number_of_wheels

    @classmethod
    def get_total_created(cls):
        print(f"Total Cars : {cls._total}")

    def __str__(self):
        return f"Model: {self.get_model_name()}, Fuel Type: {self.get_fuel_type()}, Number of Doors: {self.get_number_of_doors()}, Color: {self.get_color()}, Number of Wheels: {self.get_number_of_wheels()}"















