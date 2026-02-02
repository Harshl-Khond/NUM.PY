import numpy as np

np.random.seed(10)
marks = np.random.randint(30, 101, size=(20, 4))
print(marks)

# STEP 2 – Basic Inspection

# Print:
# Shape
# Data type
# First 5 students’ marks

print(marks.shape)
print(marks.dtype)
print(marks[:5])

# STEP 3 – Data Cleaning (IMPORTANT 🔥)
# Rules:
# Any mark below 40 → replace with 40 (grace marks)


# Any mark above 95 → cap at 95
# 👉 Use vectorized operations (where or clip)

# print(np.where(marks<40, 'marks==40'))
# print(np.clip(marks,))


# STEP 4 – Subject-wise Analytics (axis = 0)
# Calculate:
# Average marks per subject
# Highest marks per subject
# Lowest marks per subject

print(np.average(marks, axis=0))
print(np.max(marks,axis=0))
print(np.min(marks,axis=0))

# STEP 5 – Student-wise Analytics (axis = 1)
# Calculate:
# Total marks per student
# Average marks per student
# Find topper student index + total marks

print(np.sum(marks,axis=1))
print(np.average(marks,axis=1))

x=np.sum(marks,axis=1)
print(x)
y=np.argsort(x)
print(np.max(y))

# STEP 6 – Performance Classification (ADVANCED 🔥)
# Using np.where() classify students based on average marks:
# "Excellent" → avg ≥ 85
# "Good" → avg ≥ 70 and < 85
# "Needs Improvement" → avg < 70

z=np.average(marks, axis=1)
y1=np.where(z > 85,"Excellent","good")
print(y1)

y2=np.where(z >= 70,"Excellent","good")
print(y2)