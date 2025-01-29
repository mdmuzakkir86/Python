# ************* Encapsulation ****************
# Encapsulation in Python describes the concept of bundling data and methods within a single unit
# Using encapsulation we can hide an object’s internal representation from the outside-
# This is called information hiding

# Encapsulation is a way to can restrict access to methods and variables from outside of class.
# Whenever we are working with the class and dealing with sensitive data,
# providing access to all variables used within the class is not a good choice.
# prevent accidental data modification by creating private data members and methods within a class

# *************** Access Modifiers in Python **************
# Python provides three types of access modifiers private, public, and protected.
#     1.Public Member: Accessible anywhere from outside of class.
#     2.Private Member: Accessible within the class
#     3.Protected Member: Accessible within the class and its sub-classes

# ***************** Public Member ************


class Employee1:
    # constructor
    def __init__(self, name, salary):
        print("****** Public Member *******")
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)


# creating object of a class
emp1 = Employee1('Shahed', 25000)

# accessing public data members
print("Name: ", emp1.name, 'Salary:', emp1.salary)

# calling public method of the class
emp1.show()
print()


# ************ Private Member **************
# 1.To define a private variable add two underscores as a prefix at the start of a variable name

class Employee2:
    # constructor
    def __init__(self, name, salary):
        print("******* Private Member *******")
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # We have to use public method to access private members
    def display(self):
        print("name:", self.name, "salary:", self.__salary)


# creating object of a class
emp2 = Employee2('Raju', 30000)
emp2.display()

# accessing private data members out of class
# print('Salary:', emp.__salary)    # AttributeError: 'Employee' object has no attribute '__salary'
print()


# ********* Protected Member **********
# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "vLess"


# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)


c = Employee("Muzakkir")
c.show()

# Direct access protected data member
print('Project:', c._project)
print()


# We can access private members from outside of a class using the following two approaches
# 1.Create public method to access private members
# 2.Use name mangling

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()
print()


# ****| Name Mangling to access private members |
# We can directly access private and protected variables from outside of a class through name mangling
# The name mangling is created on an identifier by adding two leading underscores and one trailing underscore,
# like this _classname__dataMember

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self._Employee__salary = salary
        self.name = name
        # private member
        self.__salary = salary


# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
