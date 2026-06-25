class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

car1 = Car("SUV", "toyota", 4500)
print(car1.brand)
print(car1._model)
print(car1._Car__price)

#inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model

class Car(Vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.__price = price
car2 = Car("SUV", "toyota", 4500)
print(car2.brand)
print(car2._model)
print(car2._Car__price)

#abstraction
from abc import ABC, abstractmethod

class AbstractCar(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model

    @abstractmethod
    def start_engine(self):
        pass

class Car(AbstractCar):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.__price = price

    def start_engine(self):
        print("Engine started!")

car3 = Car("SUV", "toyota", 4500)
car3.start_engine()