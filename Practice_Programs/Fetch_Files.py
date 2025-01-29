# Printing different types of files from a directory

import os
import glob

# listing files root level using listdir() method
path = r"C:\MyLearnings\Python_Programs"
files = os.listdir(path)
for filename in files:
    print(filename)
print("-----------------------------------------------------")


# listing particular extension file
path2 = r"C:\MyLearnings\Python_Programs\\"
g = glob.glob(path2 + "*.txt")
for j in g:
    print(j)
print("-----------------------------------------------------------------")
