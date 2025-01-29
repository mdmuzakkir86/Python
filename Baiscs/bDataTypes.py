# DataTypes
""" Python provides various standard data types that define the storage method on each of them.
    The data types defined in Python are given below.
    1.Numbers
    2.Sequence Type
    3.Boolean
    4.Set
    5.Dictionary """

print("| Numbers |")
a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1 + 3j
print("The type of c", type(c))
print(" c is a complex number:", isinstance(1 + 3j, complex))
print(" b is a complex number:", isinstance(40.5, complex))
print(" a is a int number", isinstance(5, int))
print("-----------")

print("Sequence Type")
s1 = "hello"
s2 = "How are you"
print(s1[0:2])  # printing first two character using slice operator
print(s1[4])  # printing 4th character of the string
print(s1 * 2)  # printing the string twice
print(s1 + s2)  # printing the concatenation of str1 and str2
print("-----------")

print(" List ")
list1 = ["Muzakkir", 101, "Java"]
list2 = ["Umar", 102, "Python"]
# Checking type of given list
print(type(list1))

# Printing the list1
print(list1)

# List slicing
print(list1[2:])

# List slicing
print(list1[0:2])

# List Concatenation using + operator
print(list1 + list1)

# List repetation using * operator
print(list1 * 3)
print("-----------")

print("| Tuple |")
tup1 = ("Muzakkir", 101, "Java")
print(type(tup1))

# Printing the tuple
print(tup1)

# Tuple slicing
print(tup1[1:])
print(tup1[0:2])

# Tuple concatenation using + operator
print(tup1 + tup1)

# Tuple repatation using * operator
print(tup1 * 3)

# Adding value to tup. It will throw an error.
# t[2] = "hi"
print("-----------")

print("| Dictionary |")
dic = {"Name": "Muzakkir", "Roll NO": 101, "Course": "Python"}
print(dic)
print(dic.keys())
print(dic.values())
print("-----------")

print("| Boolean |")
# Python program to check the boolean type
print(type(True))
print(type(False))
# print(false)
print("-----------")

print("| SET |")
set1 = {"Muzakkir", 101, "Java"}
# Printing Set value
print(set1)
# Adding element to the set
set1.add(10)
print("After adding to set1:", set1)
# Removing element from the set
set1.remove(10)
print("List After removing:",set1)
