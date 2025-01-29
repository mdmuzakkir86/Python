"""
******| File Handling |******
1. When we want to store data permanently we required file
2. There are two types of files
    a.Text file - to store character data
    b.Binary file - to store video, audio, image and zip files etc.

Two basic and must operation of are
1. open a file : f=open(filename, mode)
    f=open(text.txt, 'w')
2. close a file: f.close

****| Different modes for a text files are |****
r, w, a, r+, w+, a+, x

1.r:
---
    open an existing file for read operation
    f=open('text.txt')
    This is the default mode
    If the specified file not found FileNotFoundError we get

2.w:
---
    f=open('text.txt', 'w')
    open an existing file for write operation
    file available but contain some data will be overwrite
    if file not available then file will be created

3.a:
---
    f=open('text.txt', 'a')
    open an existing file for append operation
    file available but contain some data and new data get append to the file no loss of data

4.r+: first read the data and then overwrite the data
5.w+: first overwrite the data then read the new written data
6.a+: append and read
7.x:
----
    to open a file in exclusive mode for write operation
    f=open('text.txt', 'x')
    if the specified file already available FileExistError we get

******| Different modes for binary file |*****
rb, wb, ab, r+b, w+b, a+b, xb

*****| Getting properties of files |*****
1. f.name -->  return name of opened file
2. f.mode -->  return mode of opened file
3. f.closed --> return boolean value

4. f.readable()
5. f.writable()
"""

# Creating a file in current directory
# Using w mode
file = open('Fruits.txt', 'w')  # If file dose not exist file will be created and get open
file.write("Apple color is red\nBanana color is yellow")  # writing to a file
print("File writable:", file.writable())
file.close()  # Closing file
print("file type is       : ", type(file))
print("file return object : ", file)
print("File name:{} | File mode: {} | File closed: {} |File Readable: {}"
      .format(file.name, file.mode, file.closed, file.readable()))

print()
print("---------------------------------------------------------------------")

# Using 'a' mode
file = open('Fruits.txt', 'a')
file.write("\nPinapple color is green\nGrapes color is green\nOrange color is orange")
file.close()

# Using 'r' mode
# f.read() --> to read all lines
# f.read(n) --> to read 'n' character from line
# f.readline() --> to read one line
# f.readlines() --> to read all lines

file = open('Fruits.txt', 'r')
# print(file.read())  # Read all lines
# print(file.read(10))  # Read only 10 characters

print(file.readline(), end='')  # Read only one line
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
file.close()

print('\n')
print("---------------------------------------------------------------------")

print("----Read all lines at a time----")
file = open('Fruits.txt', 'r')
for line in file.readlines():
    print(line, end='')
file.close()
print()
print("---------------------------------------------------------------------")

# Coping One file all data to another file
file = open('Fruits.txt', 'r')
file2 = open('Fruits2.txt', 'w')
file2.write(file.read())
file.close()
file2.close()

print("File copied successfully")
print("---------------------------------------------------------------------")

# *****| with statement |*****
# While using with statement we no need to worry about file closed or not
# because with statement will close the file
with open('Fruits2.txt', 'a') as file2:
    file2.write("\nMango color is Yellow")
print('Fruits2 opened')
print("Closed:", file2.closed)

print()
print("---------------------------------------------------------------------")

# ****| Enter data and file name dynamically |****

fName = input("Enter file name:")
file3 = open('C:\\MyLearnings\\Python_Programs\\'+fName, 'a')
data = input("Enter fruit with its color:")
file3.write(data)
# print(data)
print("File name:{} | File mode: {} | File closed: {} |File Readable: {}"
      .format(file3.name, file3.mode, file3.closed, file3.readable()))

file3.close()
