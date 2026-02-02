import numpy as np

a=np.arange(1,17)
print(a)
b=a.reshape(4,4)
print(b)
arr = np.array([[10,20],
                [30,40],
                [50,60]])

c=arr.flatten()
print(c)
print(c.shape)

d=arr.ravel()
print(d)
print(d.shape)

x = np.array([55, 20, 90, 40])
print(np.sort(x))
print(np.argsort(x))