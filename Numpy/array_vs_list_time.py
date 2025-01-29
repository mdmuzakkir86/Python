# import numpy as np
# import time

# # Creating a list with 1000000 elements
# my_list = list(range(1000000))

# # Creating a numpy array with 1000000 elements
# my_array = np.array(range(1000000))

# # Multiplying each element of the list/array by 2 and measuring the execution time
# start_time = time.time()
# my_list2 = [x * 2 for x in my_list]
# print("Execution time for list:", time.time() - start_time)

# start_time = time.time()
# my_array2 = my_array * 2
# print("Execution time for numpy array:", time.time() - start_time)


# print(my_array.ndim)

# a = np.array([[1,2,3],[1,2,3]])
# print(a.ndim)


import numpy as np  
a = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print("Array Size:",a.size)  
print("Shape:",a.shape)  

b = a.reshape(2,3)
print(b)

# import numpy as np  
# a = np.array([[1,2],[3,4],[5,6]])  
# print("printing the original array..")  
# print(a)  
# a=a.reshape(2,3)  
# print("printing the reshaped array..")  
# print(a)  
