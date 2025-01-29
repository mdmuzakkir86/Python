"""
Two important methods in python
1.tell():
---------
    To return current position of the cursor(file pointer) from beginning of the file

2.seek():
---------
    To change the position of the cursor in a file
"""

# tell() method
# Creating a file in desired location
f = open('C:\\Python_Programs\\Practice.txt', 'r+')
print(f.tell())
print(f.read(10))
print(f.tell())
print()

# seek() method
with open('File_handling.txt', 'r+') as f:
    print(f.read())
    print()
    print("Current position of cursor:", f.tell())
    f.seek(71)
    print("Current position of cursor:", f.tell())
    f.write('good!')
    print("Current position of cursor:", f.tell())
    f.seek(0)
    print("Current position of cursor:", f.tell())
    print()
    print("Data after modification")
    print(f.read())
