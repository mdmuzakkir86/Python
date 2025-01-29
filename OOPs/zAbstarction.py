# abstract base class work
# Abstraction is used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function, but inner working is hidden
# We need to import the abc module, which provides the base for defining Abstract Base classes (ABC)
# Abstraction can be achieved by using abstract classes and interfaces.

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")


car = Car()

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
