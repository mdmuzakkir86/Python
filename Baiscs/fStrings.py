# Strings
""" Python string is the collection of the characters surrounded by
    1.single quotes,
    2.double quotes,
    3.triple quotes - basically used for multiple line string """

str1 = 'Hello'
str2 = "Pyhton"
str3 = '''This is my-
first python program'''

print(str1)
print(str2)
print(str3)

print("-------------------------")
# String Indexing - string starts from 0 indexing

print("String Indexing")
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
# print(str1[5]) # IndexError: string index out of range
print("------------------------")

# `String Slicing used to access sub-string from string

print("str1[:] : ", str1[:])
print("str1[0:] : ", str1[0:])
print("str1[:1] : ", str1[:1])
print("str1[:2] : ", str1[:2])
print("str1[:3] : ", str1[:3])
print("str1[:4] : ", str1[:4])
print("str1[:5] : ", str1[:5])
print("---------------------------------")

str2 = "MUZAKKIR"
print(str2)
print("str2[0:1] : ", str2[0:1])
print("str2[2:8] : ", str2[2:8])
print("str2[9:2] : ", str2[9:2])
print("str2[5:8] : ", str2[5:8])
print("---------------------------------")

str3 = "CAPGEMINI"
print(str3)
print("str3[-1] : ", str3[-1])
print("str3[-2] : ", str3[-2])
print("str3[-3] : ", str3[-3])
print("str3[-4] : ", str3[-4])
print("str3[-5] : ", str3[-5])
print("str3[-6] : ", str3[-6])
print("str3[-7] : ", str3[-7])
print("str3[-8] : ", str3[-8])
print("str3[-9] : ", str3[-9])

print("str3[-9:-6] : ", str3[-9:-6])
print("str3[-6:]   : ", str3[-6:])
print("srt3[::-1]  : ", str3[::-1])
print("----------------------------------------------")

# String dose not support reassigning and deletion

# in and not-in

print("CAP in str3   : ", "CAP" in str3)
print("Hello in str3 : ", "Hello" in str3)
print("Hello in str3 : ", "Hello" not in str3)
print("-----------------------------------------------")

# r/R and % in String
print(R'D://Python_Programs')
print("The String str3 : %s" % str3)
print("-----------------------------------------------")

# Python String Formatting
# str4 = "They said "He is good"" #SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Above syntax solved in three ways as below

# 1.Triple Quotes
str4 = """They said, 'Capgemini's employees are good"""
print(str4)
# 2.escaping single quotes
str5 = 'They said, "Capgemini\'s Employees are good"'
print(str5)
# 3.escaping double quotes
str6 = "They said, \"Capgemini's employees are good\""
print(str6)
print("------------------------------------------------")
print("\a")
print("Hello \b World")
print("Hello \nWorld")
print("Hello \rWorld")
print("Hello\tWorld")
print("------------------------------------------------")

# The format() method
print("{} {} employees are good".format("Capgemini", "employees"))

str7 = 20
str8 = 30
print("{} dose not equals to {}".format(str7, str8))
print("------------------------------------------------")

# Python String Formatting Using % Operator
integer = 10
floatValue = 10.0
stringValue = "Hello"
print("Hi I am Integer ... My value is : %d\nHi i am Float ... My value is : %f\nHi i am String ... My vlaue is : %s"
      % (integer, floatValue, stringValue))
