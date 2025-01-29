# Creating a set
# set is unordered
# Set don't allow duplicates
# Set is mutable

set1 = {"Muzakkir", 101, 500.00}
print("set1 : ", set1)

# Traversing Set
for i in set1:
    print(i)
print("--------------------------")

# Using set() method
set2 = ({"Laptop", 12000, "Dell"})
print("set2 : ", set2)

# Set not allow mutable elements like- list, dictionary, set
# set3 = {"laptop", 13000, "HP", [10, 20]} # TypeError: unhashable type: 'list'
set3 = {"laptop", 13000, "HP"}
print("set3 : ", set3)
print("-----------------------------------------")

# Empty curly braces will create dictionary
set4 = {}
print(type(set4))

# Empty set using set() function
set5 = set()
print(type(set5))

# Trying to add duplicate elements in set
set6 = {1, 2, 2, 3, 4, 6, 7, 4, 6, 9, 5}
print("set6 : ", set6)  # {1, 2, 3, 4, 5, 6, 7, 9}
print("------------------------------------------")

# Using add() in set we can add only single element at a time
set7 = {'Hyd', 'MBNR', 'NGKL', 'KLKTY'}
print("Original se7 : ", set7)
set7.add("RR")
print("set7 after using add(\"RR\") : ", set7)
print("------------------------------------------")

# Using update() in set we can add multiple elements at a time
set8 = {'Hyd', 'MBNR', 'NGKL'}
print("Original set8 : ", set8)
set8.update(["RR", 'KLKTY'])
print("set8 after using add(\"RR\") : ", set8)
print("------------------------------------------")

# Using discard() method
set9 = {'MBNR', 'KLKTY', 'NGKL', 'RR', 'Hyd'}
print("set9 : ", set9)
set9.discard("RR")
print("set9.discard(\"RR\") : ", set9)
set9.discard("a")
print(set9)
print("------------------------------------------")

# Using remove() function
set10 = {'MBNR', 'KLKTY', 'NGKL', 'RR', 'Hyd'}
set10.remove("RR")
print("set10.remove(\"RR\") : ", set10)

# set10.remove("a") # KeyError: 'a' because 'a' is not an element of set10
print("------------------------------------------")

# Using pop() methods for removing
set11 = {'MBNR', 'KLKTY', 'NGKL', 'RR', 'Hyd'}
set11.pop()  # it remove elements randomly in set
print("set11 : ", set11)
print("------------------------------------------")

# clearing elements from set using clear() method
set12 = {'MBNR', 'KLKTY', 'NGKL', 'RR', 'Hyd'}
set12.clear()
print("set12 : ", set12)
print("------------------------------------------")
