# Create File in current directory or relative path and write to it
import glob
import os

# import shutil
from datetime import datetime

# verifying the result by printing the file present in current directory
g = glob.glob("*.txt")
for i in g:
    print(i)
print()
print("----------------------------------------------------------------------")

# Creating a file in other directory
# with statement use to open a file, it dose't required to close explicitly
# with statement automatically close file after performing operations
path = r"C:\MyLearnings\Python_Programs\\"
with open(path + "sample.txt", 'w') as file:
    file.write("Hello I am Muzakkir, practicing File Handling in python.")
    pass

g = glob.glob(path + '*.txt')
for i in g:
    print(i)
print()
print("----------------------------------------------------------------------")
#
# # Create a File If Not Exists
file_path = '{}Fruits3.txt'.format(path)
if os.path.exists(file_path):
    print(" File already exist")
else:
    with open(file_path, 'w') as file3:
        file3.write("Written to file which already exist")

temp = glob.glob(path + '.txt*')
for i in temp:
    print(i)
print()
print("---------------------------------------------------------------------")
#
# # Handling Error if file already exist, using x  mode
try:
    with open(file_path, 'x') as file4:
        pass
except:
    print("File already exist with this name")

print()
print("---------------------------------------------------------------------")

# current date as file name
x = datetime.now()
print(x)

fileName = path + x.strftime('%d-%m-%y.txt')
with open(fileName, 'w') as file5:
    file5.write("Date and time")
    print('Created', fileName)
print()
print("----------------------------------------------------------------------")

# # Reading file using read mode
with open(file_path, 'r') as file6:
    content = file6.readline()
print(content)
print()
print("-----------------------------------------------------------------------")

# # Opening a File in Append Mode
# # with open(r"C:\TEMP\File_Handling2.txt", 'a') as file:
# #     file.write("Enjoying while learning")
# #     print("Updated")
# #     pass
#
# # ******************************* Print content in a next line ******************************************
#
# file7 = open(r"C:\TEMP\File_Handling2.txt", 'a+')
# file7.write("\nEnjoying")
# file7.close()
#
# path = r"C:\TEMP\\"
# g = glob.glob(path + '*.txt')
# for i in g:
#     print(i)
# print()
# print("-----------------------------------------------------------------------")
#
# # write() method implementation
# fp = open(r"C:\TEMP\write_demo.txt", 'w')
# fp.write('This is new content')
# fp.close()
#
# file_path = r"C:\TEMP\write_demo.txt"
# fp = open(file_path, 'r')
# print(fp.read())
# fp.close()
#
# # overwriting existing content of a file
# fp = open(file_path, 'w')
# fp.write("write() method overwritten the content")
# fp.close()
#
# # Read file
# fp = open(file_path, 'r')
# print(fp.read())
# fp.close()
# print()
# print("---------------------------------------------------------------------")
#
# #   writelines(): Write a list of lines to a file
# person_data = ['\nName:Muzakkir', '\nAdress:Mahabubngar', '\nEmail:md.muzakkir@gmail.com']
# fp = open(file_path, 'a')
# fp.writelines(person_data)
# fp.close()
# print("writelines() method allow to write list in file")
# print()
# print("----------------------------------------------------------------------")
#
# # rename() method
# # os.rename('C:\TEMP\write_demo.txt', 'C:\TEMP\writeDemo.txt')
# print("file name has been changed")
# print()
# print("----------------------------------------------------------------------")
#
# # Rename a file after checking whether it exists
# try:
#     os.rename(r"C:\TEMP\10-12-21.txt", r"C:\TEMP\File_Handling5.txt")
# except:
#     print("File name already exist")
#     print("Removing Existed file")
#     # os.remove(r"C:\TEMP\File_Handling3.txt")
#
# print("-------------------------------------------------------------------------")
#
# # Copy Single File
# src_path = r'C:\TEMP\File_Handling5.txt'
# dest_path = r'C:\TEMP2\File_Handling5.txt'
# shutil.copy(src_path, dest_path)
# print("copied")
#
# # seek() doubt
