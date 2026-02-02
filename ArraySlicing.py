import numpy as np

# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].

a=np.array([10,20,30,40,50,60,70,80,90,100])
print(a[4:5])
print(a[1:7:2])
print(a[:6])
print(a[5:])
print(a[::5])
print(np.zeros(5))
print(a)
print(np.ones(5))
print(np.arange(1, 11))
print(np.arange(1, 11, 5))
print(a.size)    # number of elements
print(a.dtype)   # data type
print(a.ndim)    # number of dimensions