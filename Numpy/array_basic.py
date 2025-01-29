import numpy as np

a = np.array([10,20,30])
b = np.array([1,2,3])

def dot_product():
    result = 0
    for m,n in zip(a, b):
        result = result + a*b
    print(result)

dot_product()