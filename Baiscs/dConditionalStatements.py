# Conditional Statements
""" 1.If Statement
    2.If - else Statement
    3.Nested if Statement """

# If Statement
print("--If Statement--")
num = int(input("Enter a number to check even odd:"))
if num % 2 == 0:
    print(num, " is even number")
print("-------------------")

# If - else Statement
print("--If Else Statement--")
age = int(input("Enter your age:"))
if age > 18:
    print("Your Major")
else:
    print("Your Minor")

print("-------------------")

# Nested if Statement
print("--elif statement--")
marks = int(input("Enter the marks? "))
if 85 < marks <= 100:
    print("Congrats ! you scored grade A ...")
elif 60 < marks <= 85:
    print("You scored grade B + ...")
elif 40 < marks <= 60:
    print("You scored grade B ...")
elif 30 < marks <= 40:
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")

print("------------------------------")
