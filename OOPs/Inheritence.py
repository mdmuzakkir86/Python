"""
    Inheritance is OOPs concept in which
    child class is derived from parent class and
    child class inherits all the properties of parent class

    Types of Inheritance:
    1.Single inheritance        : one child class derived from one parent class
    2.Multiple Inheritance      : one child class derived from multiple parent class
    3.Multi-level Inheritance   : a child class is again derived by another child class
    4.Hierarchical Inheritance  : One parent class derived multiple parent class
    5.Hybrid Inheritance        : inheritance is consists of multiple types or a combination of different inheritance
"""


# ***************** Single Inheritance *********************
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parent class Constructor")

    def person(self):
        print("name:", self.name, ",", "age:", self.age)
        print("Parent class method")


# deriving child class from Parent class Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print("Child class constructor")

    def stuID(self):
        print("Student id:", self.student_id)


# print("Parent class object creation and calling method")
# person = Person("Muzakkir", 22)
# person.person()
# print()

# We could not call child class methods and members from parent class if we call error occurs
# Error 'Person' object has no attribute 'student'
# person.study(101)

student1 = Student("Muzakkir", 22, 101)
student1.person()  # Using child class object we can call parent class methods and members
student1.stuID()
print("")


# ************ Multiple Inheritance **************
class Employee:
    print("********| Multiple Inheritance |********")

    def __init__(self, designation):
        self.designation = designation

    def empDetails(self):
        print("Employee designation:", self.designation)


class Engineer(Person, Employee):
    def __init__(self, name, age, designation, role):
        Person.__init__(self, name, age)
        Employee.__init__(self, designation)
        self.role = role

    def eng_details(self):
        print("ROle:", self.role)


eng = Engineer("Hussain", 24, "Software Engineer", "Developer")
eng.person()
eng.empDetails()
eng.eng_details()
print()

# *********| Multi-level Inheritance |*********
print("*********| Multi-level Inheritance |********")


class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)

# https://appdividend.com/2019/01/22/python-super-function-example-super-method-tutorial/#:~:text=The%20super%20%28%29%20function%20in%20Python%20can%20be,superclass%20from%20the%20subclass%20that%20inherits%20from%20it
