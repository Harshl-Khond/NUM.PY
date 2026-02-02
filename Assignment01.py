import numpy as np

# Create array of numbers 1 to 20
print(np.arange(1,21))
print(np.arange(1,21,2))
print((np.arange(1,21))*10)

# Array from 1 to 10
a=(np.arange(1,11))
print(a)

# Q2 – Zeros & Ones
print(np.zeros(5))
print(np.ones(5))

# Even numbers from 2 to 20
print(np.arange(2,21,2))

# Q4 – 10 evenly spaced numbers between 0 and 1
arr = np.linspace(0, 1, 10)
print(arr)

# Q5 – Add 5 & Multiply by 3

a=np.array([10,9,8,7,6,5,4,3,2,1])
print(a+5)
print(a*3)

b=np.array([1,2,3,4,5,6,7,8,9,10])
print(a-b)
# print(a/b)
print(a+b)
print(a*b)

# Q7 – Sum, Mean, Max

print(a.sum())
print(a.mean())
print(a.max())
print(a.min())

# SECTION D – Indexing & Slicing

arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])

# Q8 – First & Last element
print(arr[0])
print(arr[-1])

# Q9 – Slicing
print(arr[2:6])   # index 2 to 5
print(arr[:4])    # first 4 elements
print(arr[-3:])   # last 3 elements

# Q10 – Change 20 → 200

arr[3] = 200
print(arr)

# SECTION E – Mini Practice

# Q11 – Print only odd numbers (1 to 15)
print(np.arange(1,16,2))   #OR

# Q12 – Replace numbers > 5 with 0

arr = np.arange(1, 11)
arr[arr > 5] = 0
print(arr)

# BONUS CHALLENGE
# Q13 – Square & Reverse (No loops)

arr = np.array([1, 2, 3, 4, 5])

squared = arr ** 2
reversed_arr = arr[::-1]

print(squared)
print(reversed_arr)

