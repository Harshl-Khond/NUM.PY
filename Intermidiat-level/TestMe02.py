import numpy as np

a=np.arange(1,25)
print(a)
print(a.size)
print(a.reshape(6,4))
print(a.reshape(3, 2, 4))



# np.arange(1, 13).reshape(4, 3)

# it gives "cannot reshape array of size 9 into shape (4,3)" because of the size of the array is 9
#  and the reshap Is 4*3 which is 12 which is not equal to the size of the array

# 🔹 SECTION 2: Axis

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [25, 35, 45]
])

print(arr.sum(axis=0))
print(arr.sum(axis=1))

# SECTION 3: Broadcasting

arr1= np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr2 = np.array([5, 10, 15])

print(arr1+arr2)
print(arr1-10)

# SECTION 4: Flatten vs Ravel
