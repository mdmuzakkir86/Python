""" Constructor initialize the variable with default values
    # In case there is no constructor defined explicitly
    # Python will place default constructor and it will be called
    There are two types of constructors
    1.Parameterized
    2.Non-Parameterized
"""


class Fruits:

    # We can declare two constructors but always latest constructor
    # will be considered by python even it is parameterized or non
    def __init__(self):
        print("First Constructor")

    def __init__(self):
        print("Second Constructor")

    def display(self, name, color):
        print("name:", name, "color:", color)


fruits1 = Fruits()
fruits1.display("Apple", "Green")
fruits2 = Fruits()
fruits2.display("Banana", "YellowS")

# ******** | Parameterized Constructor | *********
print("========= Parameterized Constructor =========")


class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Non-Parameterized Constructor")

    # Error will occur because it will become latest one
    # And we are calling parameterized constructor and this is not a parameterized constructor
    # def __init__(self):
    #     print("Parameterized Constructor")

    def show(self):
        print(self.a)
        print(self.b)


obj = A(1, 2)
obj.show()

print("========== Setter and getter methods ============")


# ********| Setter and getter methods |**********

# Accessing Attributes using Build-in methods
class Employee:
    def emp(self, name, company):
        self.name = name
        self.company = company


# creates the object of the class Employee
e = Employee()
e.emp("Muzakkir", "Capgemini")

# prints the attribute 'name' of the object e
print(getattr(e, "name"))

# reset the value of attribute 'name' to Munawar
setattr(e, "name", "Munawar")

# print name after modify
print(getattr(e, "name"))

# prints true if the student contains the attribute with name id
print(hasattr(e, "name"))
