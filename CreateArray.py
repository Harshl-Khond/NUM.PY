# Create your FIRST NumPy array

import numpy as np

a=np.array([1,2,3,4,5,6])
print(a)
print(type(a))

# Expected Output:

# [1 2 3 4 5 6]
# <class 'numpy.ndarray'>

print(np.__version__)

# 0D array: A scalar value represented as a NumPy array with zero dimensions.

b=np.array((50))
print(b)
print(type(b))

# 1D array: A one-dimensional array, similar to a list.

c=np.array([9,8,7,6,5])
print(c)
print(type(c))

# 2D array: A two-dimensional array, similar to a matrix.
d=np.array([[1,2,3,4],[9,8,7,6]])
print(d)
print(type(d))

# 3D array: A three-dimensional array, which can be thought of as a stack of matrices.

e=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(e)
print(type(e))
print(e.ndim)