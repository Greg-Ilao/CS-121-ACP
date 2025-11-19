from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Inheritance, Polymorphism
class Car(Vehicle):
    def __init__(self, brand):
        self.__brand = brand  # Encapsulation
    
    def start_engine(self):
        print(f"{self.__brand} engine started")
    
    def get_brand(self):
        return self.__brand

# Using OOP
car1 = Car("Toyota")
car2 = Car("Honda")

vehicles = [car1, car2]

for v in vehicles:   # Polymorphism
    v.start_engine()
    print("Brand:", v.get_brand())
