# List:
#       A list is a data structure in Python which is a mutable or changeable, ordered sequence of elements.
#       Each element or value that is inside of a list is called an item.
#       Just as strings are defined as characters between quotes,
#       lists are defined by having values between square brackets [ ] .

#  1. Mutable: The elements of the list can be modified.We can add or remove items to the list after it has been created
#  2. Ordered: The items in the lists are ordered. Each item has a unique index value.The new items will be added to the
#     end of the list.
#  3. Heterogenous: The list can contain different kinds of elements i.e; they can contain elements of string, integer,
#     boolean, or any type.
#  4. Duplicates: The list can contain duplicates i.e., lists can have two items with the same values.


L1 = ["Annu", 101, "MBNR"]
L2 = ["Munnu", 102, "HYD"]
print(L1, type(L1))
print(L2, type(L2))
print("L1 == L2 : ", L1 == L2)

L3 = ["Munnu", 102, "HYD"]
print("L3 == L2 : ", L3 == L2)
print("--------------------------")

# List indexing and splitting
List_Numbers = [10, 20, 30, 40, 50, 60]
print("List_Numbers[0] : ", List_Numbers[0])
print("List_Numbers[1] : ", List_Numbers[1])
print("List_Numbers[2] : ", List_Numbers[2])
print("List_Numbers[3] : ", List_Numbers[3])
print("List_Numbers[4] : ", List_Numbers[4])
print("List_Numbers[5] : ", List_Numbers[5])
print("-------------------------")

print("List_Numbers[0:]    : ", List_Numbers[0:])
print("List_Numbers[0:4]   : ", List_Numbers[0:4])
print("List_Numbers[:]     : ", List_Numbers[:])
print("List_Numbers[2:5]   : ", List_Numbers[2:5])
print("List_Numbers[0:6:2] : ", List_Numbers[1::3])
# [start-index : end-index : steps]
# start-index: count starts from given index
# steps : print the value after count value
# Ex: if start-index is 1 and step is 2,
# then count starts from index 1 in list and the value after every two counts will print and index value 1 prints
print("-------------------------")

# Negative splitting
print("List_Numbers[-1]    : ", List_Numbers[-1])
print("List_Numbers[-6:-1] : ", List_Numbers[-6:-1])
print("List_Numbers[:-1]   : ", List_Numbers[:-1])
print("List_Numbers[-4:-2] : ", List_Numbers[-4:-2])
print("List_Numbers[::-1]  : ", List_Numbers[::-1])
print("--------------------------")

# Updating List values
ListValues = [10, 20, 30, 40, 50]
print("ListValues    : ", ListValues)
ListValues[1] = 40
print("Upadated List : ", ListValues)
ListValues[1:3] = [89, 78]
print("Update multiple values : ", ListValues)
ListValues[-1] = 60
print("Adding values at the end of tht list : ", ListValues)
print("---------------------------")

# deleting elements by value
# remove() used to delete elements by value
list12 = [25, 36, 45, 86, 58, 69, 59, 85, 35]
print("List :", list12)
list12.remove(25)
# List.remove(29)  # ValueError: list.remove(x): x not in list
print("After remove : ", list12)
print("--------------------------")

# deleting values by index-value
# pop() used to delete element by index-value
# pop() returns the deleted elements
print("List12 : ", list12)
list12.pop(0)
pop_return = list12.pop(-1)
print("After pop   : ", list12)
print("pop_return  : ", pop_return)
print("--------------------------")

# del variable
print("list12", list12)
del list12[5]
print("After delete item at 5th index  :", list12)
del list12[2:4]
print("After delete item at 2 to 4 :", list12)
print("--------------------------")

# clear
list12.clear()
print("will clear return any value : ", list12)
print("After clear : ", list12)

# Iterating List
List1 = [2, 3, 4, 5, 6, 6, ]
for i in List1:
    print("List1 : ", i)
print("------------------------")

# Sum of list
List3 = [3, 4, 5, 9, 10, 12, 24]
sum1 = 0
for i in List3:
    sum1 = sum1 + i
print("The sum is:", sum1)
print("------------------------")

# Remove duplicates from list
List4 = [1, 2, 2, 3, 55, 98, 65, 65, 13, 29]

# Declare an empty list that will store unique values
List5 = []
for i in List4:
    if i not in List5:
        List5.append(i)
print("Duplicates are removed : ", List5)
print("-----------------------")

#  Common in both list
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 2, 10, 6]
common = []
for x in list1:
    for y in list2:
        if x == y:
            common.append(x)
print("The common element is:", common)

print("-----------------------")

#  Adding elements to the list append(), insert(), and extend()
#  we can use also list() method to create list
print("-----insert()-----")
my_list = list([5, 8, 'Tom', 7.50])

# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list)
# Output [5, 8, 25, 'Tom', 7.5]

# insert nested list at at position 3
my_list.insert(3, [25, 50, 75])
print(my_list)
# Output [5, 8, 25, [25, 50, 75], 'Tom', 7.5]

print("-----------------------")

print("-----extend()-----")
my_list = list([5, 8, 'Tom', 7.50])

# Using extend() it add values at the end of the list
my_list.extend([25, 75, 100])
print(my_list)
# Output [5, 8, 'Tom', 7.5, 25, 75, 100]
