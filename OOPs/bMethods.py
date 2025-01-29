"""
    Method is illustrate the state and behavior or an object
    Method consist of a business logic which perform operations related to object

    ***** There are three types of methods: *****
    1.Instance methods
    2.Class method
    3.Static method

    Methods has different variations:
    1.Parameterized Method
    2.Non-Parameterized method
"""
""" Imp points 
    - Instance method used to access and modify object state
    - Class method used to access and modify class state
"""


# ****************** Instance method ***********************
# Method which consist instance variable is called instance method
# Instance method always declare with self as a parameter
# self parameter points to the class and the current object instance
# Through the self parameter, instance methods can freely access attributes and other methods of the same object

class Vehicle:
    def __init__(self, name, color):
        self.name = name  # Instance variable
        self.color = color  # Instance Variable

    def car(self):
        # When we anticipate the variables will change significantly across instances,
        # we can define them at the instance level
        # Instance variable can be accessed from one method to another method using self variable

        print("Instance Method")
        print("name:", self.name, "color:", self.color)


v = Vehicle("BMW", "White")
v.car()

v1 = Vehicle("Maruthi", "Black")
v1.car()
print()


# ******************* Class Method ***********************
# Method which consist of static variable (class level variables) is called Class Method
# We can declare class method explicitly with @classmethod decorator
# Class method must be declared with cls variable as a parameter
# cls parameter that points to the class and not to the object instance
# class method can be called by Class name or reference variable
# class method only has access to this cls argument, it can’t modify object instance state
# Can access limited methods in the class. Can modify class specific details

class Vehicle:
    # static variable, it can be called by 'cls'/ class name/ reference variable
    # we use static variable when we expect variables are going to be consistent across instances
    wheels = 4  # Static variable

    @classmethod
    def car(cls, name, color):
        print("Class Method")
        print("Every car has {} wheels".format(cls.wheels), "| Using cls")
        print("Every car has", Vehicle.wheels, "Wheels | using class name")
        print("name", name, ",", "color", color)


v2 = Vehicle()
v2.car("BMW", "White")
print("every car has {} wheels".format(v2.wheels), "| using reference variable")
print()


# ******************** Static method ***********************
# We can declare static method explicitly by using @staticmethod decorator
# We can access static methods by using class name or object reference
# We use static method when we want to call method without creating an object or instantiate an instance
# static method can neither modify object state nor class state.
# Static methods are restricted in what data they can access
# Cannot access anything else in the class. Totally self-contained code

class Add:
    temp = None

    @staticmethod
    def add(*num):
        print("Static Method")
        # local variable
        # Local variables can not be accessed out method
        total = 0
        Add.temp = 2

        for n in num:
            total += n
        print("sum of:", end="")
        print(*num, sep="+", end=" = ")
        print(total)
        print("total : ", type(total))
        print('num   : ', type(num))
        print()
        print(Add.temp)


# Add.add(10, 20, 30)
# print(Add.temp)

# add = Add()
# add.temp = 10
# print(add.temp)
# print(Add.temp)

inputs = input("Enter values to add:")
inputs = tuple(map(int, inputs.split(" ")))
Add.add(inputs)
print("-----------------------------------------")

# Not working
# inputs = int(input('Enter numbers to add:').split(','))
# add(inputs)

# def add(num):
#     total = 0
#
#     for n in num:
#         total += n
#     print("sum of:", end="")
#     print(num, sep="+", end=" | ")
#     print(*num, sep='+', end=" = ")
#     print(total)
#     print('total : ', type(total))
#     print('num : ', type(num))
#
#
# inputs = input('Enter numbers to add:')
# inputs = list(map(int, inputs.split()))
# add(inputs)


"""
    https://www.delftstack.com/howto/python/split-integer-into-digits-python/#:~:text=Use%20the%20map%20%28%29%20and%20str.split%20%28%29%20Functions,used%20to%20split%20a%20string%20into%20a%20list.
    https://realpython.com/instance-class-and-static-methods-demystified/
"""
