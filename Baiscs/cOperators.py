# Operators in python
""" 1.Arithmetic operators
    2.Comparison operators
    3.Assignment Operators
    4.Logical Operators
    5.Bitwise Operators
    6.Membership Operators
    7.Identity Operators """

print("| Arithmetic Operators |")
print("--Addition--")
print("20+30=", 20 + 30)
print("--Subtraction--")
print("10-20=", 10 - 20)
print("--Multiplication--")
print("10*10=", 10 * 10)
print("--Division--")
print("100/10=", 100 / 10)
print("--Reminder--")
print("100%10=", 100 % 3)
print("--Floor Division--")
print("17//3=", 17 // 3)
print("--Exponent--")
print("3**3=", 3 ** 3)

print("--------------------------")

print("| Comparison Operator |")
print("--Equals To--")
a = 10
b = 11
print("--Equal To--")
print("a==b:", a == b)
print("--Not Equal To--")
print("a!=b:", a != b)
print("--Greater Than--")
print("a>b:", a > b)
print("--Less Than--")
print("a<b:", a < b)
print("--Greater Than or Equals to--")
print("a>=b:", a >= b)
print("--Less Than or Equals to--")
print("a<=b:", a <= b)

print("----------------------------------")
# Assignment Operators
print("| Assignment Operators |")
print("--‘=’ Operator--")
c = 100
print('The initial value of variable c is ', c)
print("--‘+=’ Operator--")
c += 50
print('c += 50:', c)
print("--‘-=’ Operator--")
c -= 50
print("c -= 50:", c)
print("--‘*=’ Operator--")
c *= 10
print("c *= 10:", c)
print("--‘/=' Operator--")
c /= 5
print("c /= 5:", c)
print("--‘%=’ Operator--")
c %= 3
print("c %= 3:", c)
print("--‘//=' Operator--")
c //= 7
print("c //= 7:", c)
print("--‘**=' Operator--")
c **= 2
print("c **= 2:", c)

print("------------------------")

# Logical Operators
print("| Logical Operators |")
print("--AND Operator--")
x = 20
y = 50
if x >= 10 and y == 50:
    print("x >=10 and y ==50:True")
else:
    print("False")

print("--OR Operator--")
if x < 10 or y > 50:
    print("x < 30 or y > 30:True")
else:
    print("False")

print("----------------------------")

# Bitwise Operators
print("| Bitwise Operators |")
 
a = 10
b = 4
 
# Print bitwise AND operation
print("a & b =", a & b)
 
# Print bitwise OR operation
print("a | b =", a | b)
 
# Print bitwise NOT operation
print("~a =", ~a)
 
# print bitwise XOR operation
print("a ^ b =", a ^ b)
