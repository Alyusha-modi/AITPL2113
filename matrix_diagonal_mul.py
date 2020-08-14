import numpy as np

arr1 = np.array([[2, 0, 0, 0], [0, 7, 0, 0],[0, 0, 6, 0],[0, 0, 0, 8]])
arr2=np.array([[1,2],[3,4],[5,6],[7,8]])
print('Both the Arrays:')
print(arr1)
print(arr2)
arr_result = np.matmul(arr1, arr2)
print(f'Matrix Product of arr1 and arr2 is:\n{arr_result}')


