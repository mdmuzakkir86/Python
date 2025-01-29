# for loop

# Printing values in range from 1-10
print("Printing values in range from 1-10")
for numbers in range(1, 11):
    print(numbers, end=" ")
print()

# Printing values from 11-1
print("Printing values in range from 10-1")
for numbers in range(10, 0, -1):
    print(numbers, end=" ")

print()
print("----------------------------------")

# Print last two letters and increamental order in every line of a name
name = input("Enter your name:")
lastTwoCharacters = name[-2:]
for character in range(11):
    print(lastTwoCharacters * character)
print("---------------------------------")

# Traversing the list
nameList = ["Annu", "Munnu", "Chunnu"]
for name_list in nameList:
    print(name_list)
print("---------------------------------")

# Table of a given number
n = int(input("Enter number to get its table:"))
for i in range(1, 11):
    table = n * i
    print(n, "*", i, "=", table)
print("-----------------------------------------")

# Sum of the list
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total += number
print("10+20+30+40=", total)
print("------------------------------------------")

list1 = ["annu", "munnu", "chunnu"]
for i in range(len(list1)):
    print("Hello", list1[i])

# Nested loop
rows = int(input("Enter number of rows"))
for i in range(rows + 1):
    for j in range(i):
        print("*", end='')
    print()
print("-----------------------------------------")

# While loop
i = 1
while i <= 10:
    print(i, end="")
    i += 1
print()

print("--------------------------------------------")

i = 1
n = int(input("Enter table number:"))
result = 0
while i <= 10:
    result = n*i
    print(n, "*", i, "=", result)
    i += 1
print("--------------------------------------------")
