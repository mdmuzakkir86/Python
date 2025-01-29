# Python Set Operations
""" Set can be performed mathematical operation such as
    1.union,
    2.intersection,
    3.difference, and
    4.symmetric difference """

# Union of two Sets
# Union operation Using '|' operator
set1 = {10, 20, 30, 40, 50, 60}
set2 = {70, 80, 50, 30, 90}
print("set1 | set2 : ", set1 | set2)  # {70, 40, 10, 80, 50, 20, 90, 60, 30}
print("---------------------------------------------------------")

# Union operation Using union() method
set3 = {10, 20, 30, 40, 50, 60}
set4 = {70, 80, 50, 30, 90}
print("set3.union(set4) : ", set1.union(set4))  # {70, 40, 10, 80, 50, 20, 90, 60, 30}
print("---------------------------------------------------------")

# The intersection_update() method
set5 = {10, 20, 30, 40, 50, 60}
set6 = {70, 80, 50, 30, 90}
# Removing elements from set5 which are common in set6
# OR
# printing set5 elements those are matching in set6
set5.intersection_update(set6)
print(set5)  # {50, 30}
print(set6)
print("--------------------------------------------------------")

# Difference between the two sets
# Using subtraction ( - ) operator
set7 = {10, 20, 30, 40, 50, 60}
set8 = {70, 80, 50, 30, 90}
# Removing the elements from set7 which are not matching in set8
print("set7-set8 : ", set7 - set8)  # {40, 10, 20, 60}
print("----------------------------------------------------------")

#  Using difference() method
set9 = {10, 20, 30, 40, 50, 60}
set10 = {70, 80, 50, 30, 90}
print("set9.difference(set10) : ", set9.difference(set10))  # {40, 10, 20, 60}
print("----------------------------------------------------------")

# Symmetric Difference of two sets
# Using ^ operator
set11 = {10, 20, 30, 40, 50, 60}
set12 = {70, 80, 50, 30, 90}
# Printing the elements those are not common in both sets
set13 = set11 ^ set12  # {70, 10, 80, 20, 90, 40, 60}
print(set13)
print("----------------------------------------------------------")

# Using symmetric_difference
set14 = {10, 20, 30, 40, 50, 60}
set15 = {70, 80, 50, 30, 90}
# Printing the elements thos are not common in both sets
set16 = set14.symmetric_difference(set15)  # {70, 10, 80, 20, 90, 40, 60}
print(set16)
print("----------------------------------------------------------")
