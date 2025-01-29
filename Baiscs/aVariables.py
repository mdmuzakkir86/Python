# Variables practice

""" Variables can declared in three different ways
    1.Camel case : first word letter should be small and every new middle word first letter should be Capital
    2.Pascal case: In the camel case, each word or abbreviation in the middle of begins with a capital letter
    3.Snake case :  In the snake case, Words are separated by the underscore """

print("Camel case|Pascal case|Snake case")
nameOfStudent = "Md"  # Camel case
NameOfStudent = "Muzakkir"  # Pascal case
name_of_student = "Sahab"  # Snake case
print(nameOfStudent, NameOfStudent, name_of_student)
print("-------------")

# Variables are case sensitive
# Multiple Assignment variables
print("Multiple Assignment variables")
a = b = c = 30
d, e, f = 10, 20, 30
total = a + b + c + d + e + f
print(a, b, c)
print(d, e, f)
print("total:", total)
print("------------")

# Types of Variables
""" Variables are two types
    1.Local variable: Local variables are the variables that declared inside the function and have scope 
      within the function
    2.Global variable: Global variables can be used throughout the program, and its scope is in the entire program. 
      We can use global variables inside or outside the function."""


def practice():
    print('Local variable')
    g = 10  # Local variable
    h = 20  # Local variable
    sum_value = g + h  # local variable
    print("g+h:", sum_value)


practice()

bike = " "


def practice_two():
    print('Global variable')
    global bike  # declare global variable as a global
    bike = "Pulsar"  # Initializing the global variable inside of function
    bike_model = "150CC"
    bike_plate_number = "TS 07 4567"
    # noinspection PyStringFormat
    print('Bike Name: {2},  | Bike Model {0},  | Bike Number {1}'.format(bike_model, bike_plate_number, bike))


practice_two()
# print(bike_model) # local variable can not be used outside of function scope
print("-----------")
