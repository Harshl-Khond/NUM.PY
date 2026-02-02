import numpy as np

# Write code to create a NumPy array containing numbers 5 to 50 with a gap of 5.

print(np.arange(5,51,5))

# Create an array of 8 zeros and print its:
a=np.zeros(8)
print(a)
print(a.size)
print(a.ndim)
print(a.dtype)

# 🔢 PART C – Array Operations

# Given:

a = np.array([2, 4, 6, 8])
b = np.array([1, 2, 3, 4])

# Q6 Write code for:
# a + b
# a * b
# a - 1

print(a+b)
print(a-b)
print(a*b)

# Q7 Find:
# Sum of a
# Mean of b

print(a.sum())
print(b.mean())

# ✂ PART D – Indexing & Slicing (Very Important)
# Given:

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Q8 Print the third element
#    Print the second last element
print(arr[2])
print(arr[-2])

# Q9
# Print:
# Elements from 30 to 60
# First 3 elements
# Last 2 elements

c=np.arange(30,71)
print(c)
print(c[:3])
print(c[-2:])

# Q11
# Without using loops, write code to:
# Create array from 1 to 10
# Print only numbers greater than 6

x=np.arange(1,11)
print(x)
print(x[x>6])