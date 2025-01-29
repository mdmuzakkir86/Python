# Creating Tuple

# Tuple:
#       A tuple is a data structure in Python that is a immutable, or unchangeable, ordered sequence of elements.
#       Each element or value that is inside of a list is called an item.
#       Just as strings are defined as characters between quotes,
#       lists are defined by having values between parentheses ( ) .

#  1. Immutable: The elements of the tuple can't be modified.
#     We can add or remove items to the tuple after it has been created
#  2. Ordered: The items in the tuple are ordered. Each item has a unique index value.The new items will be added to the
#     end of the tuple.
#  3. Heterogenous: The tuple can contain different kinds of elements i.e; they can contain elements of string, integer,
#     boolean, or any type.
#  4. Duplicates: The tuple can contain duplicates i.e., tuple can have two items with the same values.


t1 = (10, 20, 30, 40, 50)  # tuple using ()
t2 = 10, 20, 30, 40, 50  # tuple without ()

print("t1 == t2 : ", t1 == t2, type(t1))
print("t1 != t2 : ", t1 != t2, type(t2))
print("----------------------------")


# Tuple indexing and splitting
print("t1 : {} \nt2 : {}".format(t1, t2))
print("t1[0] : ", t1[0])
print("t1[1] : ", t1[1])
print("t1[2] : ", t1[2])
print("t1[3] : ", t1[3])
print("t1[4] : ", t1[4])
# print("t1[5] : ", t1[5])
print("-------------------------")

print("t1[0:]    : ", t1[0:])
print("t1[0:4]   : ", t1[0:4])
print("t1[:]     : ", t1[:])
print("t1[2:5]   : ", t1[:5])
print("t1[0:4:2] : ", t1[0:4:3])
print("-------------------------")

# Negative splitting
print("t1[-1]    : ", t1[-1])
print("t1[-6:-1] : ", t1[-6:-1])
print("t1[:-1]   : ", t1[:-1])
print("t1[-4:-2] : ", t1[-4:-2])
print("--------------------------")

# Updating List values
print("t1 : ", t1)
# t1[1] = 40 # tuple is immutable
print("tuple is immutable")
print("----------------------------")

# Delete elements
# del t1[0]
print("TypeError: \'tuple\' object doesn\'t support item deletion")
print("----------------------------")

# Tuple Iteration
print("t2 : ", t2)
for i in t2:
    print(i)
print("----------------------------")

# Sum of tuple
t3 = (3, 4, 5, 9, 10, 12, 24)
sum1 = 0
for i in t3:
    sum1 = sum1 + i
print("The sum is:", sum1)
print("------------------------")
