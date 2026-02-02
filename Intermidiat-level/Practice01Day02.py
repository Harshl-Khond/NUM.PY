import numpy as np

a=np.array([10,20,30])
print(a.shape)
b=a.reshape(1,3)
print(b)
print(b.shape)

z=np.array([[1,2,3],[4,5,6]])
c=z.flatten()
d=z.ravel()
print(c)
print(d)
z[0]=99
print(z)
print(c)
print(d)

marks = np.array([78, 88, 67, 90])

rank = np.argsort(marks)
print(rank)