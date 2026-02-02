import numpy as np
a=np.array([[30,45,55],[46,34,56]])
print(a)
print(a.shape)
print(a.ndim)
print(a.sum(axis=0))
print(a.sum(axis=1))

# print(a.reshape(3,2))

b=np.array([44,56,73])
print(a + b)