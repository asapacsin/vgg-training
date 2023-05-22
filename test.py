import numpy as np

def relu(input):
        return np.maximum(input,0)

#read  test_case.xlsx

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1],[2]])
c = a*b
print(c)