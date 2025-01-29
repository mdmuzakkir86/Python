# Polymorphism means many forms
# Polymorphism is a main OOPS concept
# Polymorphism performed by method overriding and method overloading
# Polymorphism mostly use in inheritance


# *************| Method Overriding |*************
# In Method Overriding two or more method names and its arguments are same but having different logic
class Vehicle:
    print("| Method Overriding |")

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def vehicle_details(self):
        print("name:{}|color:{}|price:{}".format(self.name, self.color, self.price))

    def vehicle_max_speed(self, speed):
        print("Vehicle max speed is:", speed)

    def vehicle_has_gears(self, gear):
        print(" has 8 gears")


class Car(Vehicle):

    def vehicle_max_speed(self, speed):
        print("{} car max speed is 200".format(self.name))

    def vehicle_has_gears(self, gear):
        print("{} car has 7 gears".format(self.name))


class Truck(Vehicle):

    def vehicle_max_speed(self, speed):
        print("{} truck max speed is 140".format(self.name))

    def vehicle_has_gears(self, gear):
        print("{} truck has 6 gears".format(self.name))


car = Car("BMW", "White", 2500000)
car.vehicle_details()
car.vehicle_max_speed(500)
car.vehicle_has_gears(6)
print()

truck = Truck("ASHOK", "Yellow", 500000)
truck.vehicle_details()
truck.vehicle_max_speed(400)
truck.vehicle_has_gears(5)
print()


# There are 3 types of overloading
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading (Not possible)


# ************| Operator Overloading |**********

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)

class Book:
    print(" | Operator Overloading | ")

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)
print('The Total Number of Pages:', b1 + b2)
print()


# *************** Method Overloading *****************
# In python overloading is some what different  from C++ and java
# By default python do not support method overloading
# To achieve it we have different methods
# The main purpose overloading accepting number of arguments


# If we try to implement always python refer to latest define method
class Overloading1:
    @staticmethod
    def method1(a, b):
        print(a + b)

    @staticmethod
    def add(a, b, c):
        print(a + b + c)


# Overloading1.method1(20, 30) ## Error here
Overloading1.add(10, 20, 30)
print()

# Efficient method
from multipledispatch import dispatch


# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997


# Not-Efficient method

class Overloading2:
    @staticmethod
    def add(datatype, *args):
        total = None
        if datatype == 'int':
            total = 0

        if datatype == 'float':
            total = 0.0

        if datatype == 'str':
            total = ''

        for x in args:
            total += x

        print(*args, "=", total)


Overloading2.add('int', 10, 20)
Overloading2.add('float', 10.50, 10.50)
Overloading2.add('str', "Muzakkir", "Capgemini")

# *********| Constructor Overloading |************
# If we declare multiple constructors error will rise

# class Test:
#     def __init__(self):
#         print('No-Arg Constructor')
#
#     def __init__(self, a):
#         print('One-Arg constructor')
#
#     def __init__(self, a, b):
#         print('Two-Arg constructor')
#
#
# t1 = Test()
# t1 = Test(10)
# t1 = Test(10, 20)
