# print simple line
print("Hello Python")
# Declaration dose not required providing datatype separately, python analyze automatically
a = 10
print("a =", a)
b = a
print("a =", a, "= b")

# Doubt: Why value of b is not changed even a value is changed ?
# Doubt: Why python allowing duplicate variables and how ?
a = 20
_c = a
print("a= ", a, "b=", b)
print("'a' datatype is:", type(a))
print("-------------")

# Usage of 'sep' and 'end' aurguments
print("a = ", a, end='123', sep='0')

print("")
print("-------------")

# Taking input from user
name = input("Enter your name:")
print("You entered:", name)
print("name datatype is:", type(name))
print("-------------")

# Casting input to required data type
mobile_No = int(input("Enter your mobile number:"))
print("You entered:", mobile_No)
print("Mobile Number datatype is:", type(mobile_No))
print("-------------")

inputString = input("Enter a string: ").casefold()

# casefold() is to ensure that uppercase and lower case character is treated same.
# If you don't want, you can remove casefold()

# count the repeated char
tempStr = ''
for char in inputString:
    if char not in tempStr:
        print(char, inputString.count(char))
        tempStr = tempStr + char
