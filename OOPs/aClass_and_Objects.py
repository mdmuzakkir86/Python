"""
    OOPS is mainly used for re-usability of code

    Class is a user define data structure that bonds data members and methods as a single unit
    Class is a blue-print of an object
    Using class we can create on objects as many we want

 Object: Anything that has state and behavior
         state is nothing but attributes
         behavior is nothing but action
"""


class Person:

    company_name = "Capgemini"

    # _init_() is a construction which initialize the values
    # self parameter used to point current instance variable and to access the variable of current instance

    # Parameterized Constructor
    def __init__(self, name, profession):
        # Data members(Instance variables)
        self.name = name
        self.profession = profession
        print("Constructor Called Successfully")

    # Behavior (Instance method)
    def work(self):
        print(" name: ", self.name, "\n", "Profession: ", self.profession)


print(Person.company_name)
person1 = Person("Muzakkir", "Developer")  # Creating object of class
person1.work()                             # Calling method with person1 pointing object
person2 = Person("Mazhar", "Testing")      # Creating object of class
person2.work()                             # Calling method with person2 pointing object
