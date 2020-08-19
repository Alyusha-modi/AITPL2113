
import numpy
# initialize two array
x = numpy.array([[1, 2, 5], [3, 4, 7]], dtype=numpy.float64)
y = numpy.array([[3, 4], [5, 6],[8, 9]], dtype=numpy.float64)

print('Print the two matrices')
print('X = \n', x)
print('Y = \n', y)
'''
# Elementwise sum; both produce the array
print('\nElementwise addition of two matrices: ( X + Y)')
print('Add using add operator: \n', x + y)
print('Add using add function: \n', numpy.add(x, y))

# Elementwise difference; both produce the array
print('\nElementwise subtraction of two matrices: ( X - Y)')
print('Subtract using operator: \n', x - y)
print('Subtract using function: \n', numpy.subtract(x, y))

# Elementwise product; both produce the array
print('\nElementwise Multiplication of two matrices: ( X * Y)')
print('Multiply using operator: \n', y * x)
print('Multiply using function: \n', numpy.multiply(y, x))

# Elementwise division; both produce the array
print('\nElementwise division of two matrices: ( X / Y)')
print('Division using operator: \n', x / y)
print('Division using function: \n', numpy.divide(x, y))
'''
# Elementwise square root; produces the array
print('\nSquare root each element of X matrix\n', numpy.sqrt(x))

# Matrix Multiplication using dot()
print('\nMatrix Multiplication of two matrices: ( x * y)')
print(x.dot(y))

#using matmul()
arr_result = numpy.matmul(x, y)
print(f'Matrix Product of x and y is:\n{arr_result}')


