import numpy as np

x = np.array([[1,2],[3,4],[5,6],[7,8]])
y = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
z = np.array([[1, 2], [5, 6]])


# Perform Operation (x*y*z)+(y*z)+x
arr_result = np.matmul(x, y)
#arr_result1=np.matmul(arr_result,z)
print(arr_result)
#print(arr_result1)
#arr = np.matmul(y, z)
#print(arr)
