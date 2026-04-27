import math #imports a module, so that code not in this file can be accessed and used

class Car:

    cars = [] #declaring and assigning an attribute of the class 

    #__init__: method that runs when instance is created
    def __init__(self, age, model, run): #self: a reference to current instance
        self.age = age #declaring and assigning an attribute of the instance 
        self.model = model
        self.run = run

        Car.cars.append(self)
    
    #__str__: method that runs when instance is converted to str with str() or print()
    def __str__(self):
        return f"{self.model}: {self.age} years, {self.run} km"
    
    #method that can be called
    def drive(self, distance):
        self.run += distance
    
    #decoration that exstends functionality and clarity that wraps around contained functions
    @property #@property: methods that dont take arguments and can be called like attributes

    def honk():
        return "beep beep"

    @classmethod #@classmethod: methods that work with the class state instead of instance state
    
    def first_car(cls): #cls: a reference to the class
        return cls.cars[0]

    @staticmethod #@staticmethod: methods that do not access or modify instance or class state, 
    # often just for orginazation
    def calculate_distance(x_distance, y_distance):
        return math.sqrt(x_distance**2 + y_distance**2) #calls a function from a module
    

lisa = Car(12, "donson", 230) #creating a car instance and passing arguments to __init__ method
lisa.age # accessing instance attribute using dot notation

del lisa.run #deleting the run attribute from this instance
#lisa.run #accessing this attribute on this instance will cause an error

#defining a function named func tacking 2 arguments (parameters when defined)
#aguments have expected types and default values
#function is expected to return a str
def func(value1: int = 32, value2: str = "car") -> str:
    if str(value1) == value2:
        raise Exception("value1 and value2 cannot be the same")
    
    return value2



