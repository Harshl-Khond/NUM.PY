import numpy as np

a=np.array([
    [30,45,55],
    [46,34,56],
    [23,67,89]])

print(a.sum(axis=0))
print(a.sum(axis=1))

b=np.array([10,20,30])
print(a + b)