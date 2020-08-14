import numpy as np

arr1=np.array([[1,2],[3,4],[5,6],[7,8]])
arr1_transpose = arr1.transpose()
print(f'Original Array:\n{arr1}')
print(f'Transposed Array:\n{arr1_transpose}')

# multiplication using matmul()
arr_result = np.matmul(arr1, arr1_transpose)
print(f'Matrix Product of arr1 and arr1_transpose is:\n{arr_result}')
'''
# Elementwise sum; both produce the array
print('\nElementwise addition of two matrices:')
print('Add using add operator: \n', arr1 + arr1_transpose)
print('Add using add function: \n', np.add(arr1, arr1_transpose))

# Elementwise difference; both produce the array
print('\nElementwise subtraction of two matrices:')
print('Subtract using operator: \n', arr1 - arr1_transpose)
print('Subtract using function: \n', np.subtract(arr1, arr1_transpose))

# Elementwise product; both produce the array
print('\nElementwise Multiplication of two matrices: ')
print('Multiply using operator: \n', arr1 * arr1_transpose)
print('Multiply using function: \n', np.multiply(arr1, arr1_transpose))

# Elementwise division; both produce the array
print('\nElementwise division of two matrices: ')
print('Division using operator: \n', arr1 / arr1_transpose)
print('Division using function: \n', np.divide(arr1, arr1_transpose))

'''