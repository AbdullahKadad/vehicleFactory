# Vehicle Factory

This repository contains a Python implementation of a simple vehicle factory with an abstract base class `Factory` and its subclasses `Motorcycle` and `Car`. The factory keeps track of the total number of vehicles created and provides various methods for setting and getting vehicle attributes.

## Classes

### Factory

`Factory` is an abstract base class representing a generic vehicle factory. It defines common attributes and methods that must be implemented by subclasses.

#### Attributes

- `_total`: Class variable that keeps track of the total number of vehicles created.
- `_model_name`: The model name of the vehicle.
- `_fuel_type`: The fuel type of the vehicle.

#### Methods

- `__init__(self, model_name, fuel_type)`: Initializes the vehicle with a model name and fuel type. Increments the total vehicle count.
- `@classmethod get_total_created(cls)`: Prints the total number of vehicles created.
- `@abstractmethod get_model_name(self)`: Abstract method to get the model name.
- `@abstractmethod get_fuel_type(self)`: Abstract method to get the fuel type.
- `@abstractmethod set_model_name(self, value)`: Abstract method to set the model name.
- `@abstractmethod set_fuel_type(self, value)`: Abstract method to set the fuel type.
- `@abstractmethod get_number_of_wheels(self)`: Abstract method to get the number of wheels.

### Motorcycle

`Motorcycle` is a subclass of `Factory` representing a motorcycle. It adds specific attributes and methods for motorcycles.

#### Motorcycle Attributes

- `_total`: Class variable that keeps track of the total number of motorcycles created.
- `_number_of_wheels`: Number of wheels (default is 2).

#### Motorcycle Methods

- `__init__(self, model_name, fuel_type, number_of_wheels=2)`: Initializes the motorcycle with a model name, fuel type, and number of wheels. Increments the total motorcycle count.
- `get_model_name(self)`: Returns the model name.
- `get_fuel_type(self)`: Returns the fuel type.
- `set_model_name(self, value)`: Sets the model name.
- `set_fuel_type(self, value)`: Sets the fuel type. Validates that the fuel type is either 'electric', 'petrol', or 'diesel'.
- `get_number_of_wheels(self)`: Returns the number of wheels.
- `@classmethod get_total_created(cls)`: Prints the total number of motorcycles created.
- `__str__(self)`: Returns a string representation of the motorcycle.

### Car

`Car` is a subclass of `Factory` representing a car. It adds specific attributes and methods for cars.

#### Car Attributes

- `_total`: Class variable that keeps track of the total number of cars created.
- `_number_of_doors`: Number of doors.
- `_color`: Color of the car.
- `_number_of_wheels`: Number of wheels (default is 4).

#### Car Methods

- `__init__(self, model_name, fuel_type, number_of_doors, color, number_of_wheels=4)`: Initializes the car with a model name, fuel type, number of doors, color, and number of wheels. Increments the total car count.
- `get_model_name(self)`: Returns the model name.
- `get_fuel_type(self)`: Returns the fuel type.
- `set_model_name(self, value)`: Sets the model name.
- `set_fuel_type(self, value)`: Sets the fuel type. Validates that the fuel type is either 'electric', 'petrol', or 'diesel'.
- `get_color(self)`: Returns the color.
- `set_color(self, value)`: Sets the color.
- `get_number_of_doors(self)`: Returns the number of doors.
- `set_number_of_doors(self, value)`: Sets the number of doors. Validates that the number of doors is either 2 or 4.
- `get_number_of_wheels(self)`: Returns the number of wheels.
- `@classmethod get_total_created(cls)`: Prints the total number of cars created.
- `__str__(self)`: Returns a string representation of the car.

## Usage

To use the `Motorcycle` and `Car` classes, you need to create instances of these classes and use their methods. Below is an example of how to create and manipulate `Motorcycle` and `Car` objects.

```python
from vehicle_factory.motorcycle import Motorcycle
from vehicle_factory.car import Car

# Creating a Motorcycle instance
motorcycle = Motorcycle("Yamaha MT-07", "petrol")
print(motorcycle)  # Output: Model: Yamaha MT-07, Fuel Type: petrol, Number of Wheels: 2.

# Creating a Car instance
car = Car("Tesla Model 3", "electric", 4, "blue")
print(car)  # Output: Model: Tesla Model 3, Fuel Type: electric, Number of Doors: 4, Color: blue, Number of Wheels: 4

# Changing attributes
motorcycle.set_model_name("Yamaha MT-09")
motorcycle.set_fuel_type("electric")
car.set_color("red")
car.set_number_of_doors(2)

# Printing updated details
print(motorcycle)  # Output: Model: Yamaha MT-09, Fuel Type: electric, Number of Wheels: 2.
print(car)  # Output: Model: Tesla Model 3, Fuel Type: electric, Number of Doors: 2, Color: red, Number of Wheels: 4

# Getting the total created vehicles
Motorcycle.get_total_created()  # Output: Total Motorcycles: 1
Car.get_total_created()         # Output: Total Cars: 1
Factory.get_total_created()     # Output: Total Vehicles: 2
