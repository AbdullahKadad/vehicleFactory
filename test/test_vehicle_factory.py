import pytest
from vehicle_factory.motorcycle import Motorcycle  
from vehicle_factory.car import Car
@pytest.fixture
def motorcycle_instance():
    return Motorcycle("TestModel", "petrol")

def test_model_name(motorcycle_instance):
    assert motorcycle_instance.get_model_name() == "TestModel"
    motorcycle_instance.set_model_name("NewModel")
    assert motorcycle_instance.get_model_name() == "NewModel"

def test_fuel_type(motorcycle_instance):
    assert motorcycle_instance.get_fuel_type() == "petrol"
    motorcycle_instance.set_fuel_type("diesel")
    assert motorcycle_instance.get_fuel_type() == "diesel"
    try:
        motorcycle_instance.set_fuel_type("Water")
    except Exception as e:
        actual = type(e)
        expected = ValueError
    assert actual == expected

def test_number_of_wheels(motorcycle_instance):
    assert motorcycle_instance.get_number_of_wheels() == 2

def test_total_created():
    initial_total = Motorcycle._total
    Motorcycle("Model1", "petrol")
    Motorcycle("Model2", "diesel")
    assert Motorcycle._total == initial_total + 2

def test_str_method(motorcycle_instance):
    expected_str = "Model: TestModel, Fuel Type: petrol, Number of Wheels: 2."
    assert str(motorcycle_instance) == expected_str


@pytest.fixture
def car_instance():
    return Car("TestCar", "petrol", 4, "red")

def test_car_model_name(car_instance):
    assert car_instance.get_model_name() == "TestCar"
    car_instance.set_model_name("NewCarModel")
    assert car_instance.get_model_name() == "NewCarModel"

def test_car_fuel_type(car_instance):
    assert car_instance.get_fuel_type() == "petrol"
    car_instance.set_fuel_type("diesel")
    assert car_instance.get_fuel_type() == "diesel"
    try:
        car_instance.set_fuel_type("Water")
    except Exception as e:
        actual = type(e)
        expected = ValueError
    assert actual == expected

def test_car_color(car_instance):
    assert car_instance.get_color() == "red"
    car_instance.set_color("blue")
    assert car_instance.get_color() == "blue"

def test_car_number_of_doors(car_instance):
    assert car_instance.get_number_of_doors() == 4
    car_instance.set_number_of_doors(2)
    assert car_instance.get_number_of_doors() == 2
    try:
        car_instance.set_fuel_type(3)
    except Exception as e:
        actual = type(e)
        expected = ValueError
    assert actual == expected

def test_car_number_of_wheels(car_instance):
    assert car_instance.get_number_of_wheels() == 4

def test_car_total_created():
    initial_total = Car._total
    Car("Model1", "petrol", 4, "red")
    Car("Model2", "diesel", 2, "blue")
    assert Car._total == initial_total + 2

def test_car_str_method(car_instance):
    expected_str = "Model: TestCar, Fuel Type: petrol, Number of Doors: 4, Color: red, Number of Wheels: 4"
    assert str(car_instance) == expected_str
