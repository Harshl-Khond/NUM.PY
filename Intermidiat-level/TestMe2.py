import numpy as np

#Q1  axis=0 refers to columns

#Q2 fltten is refers to the copy it makes a new array , memery requred is more and safe to use 
# ravel ii update the existion array direcly if reured less memory and fast in nature as compare to the slatten
# 
# Q3 Why do we use np.random.seed()? 
# # Ans: We use np.random.seed() to set a specific starting point for the random number generator in NumPy.

# ⚙ PART B – Reshape & Axis
# Q4Create a NumPy array from 1 to 20 and reshape it into 5 rows (Use -1 for columns)

arr = np.arange(1, 21)
print(arr.reshape(5, -1))

# Q5 
arr = np.array([
    [12, 18, 25],
    [20, 30, 35],
    [15, 22, 28],
    [10, 16, 24]
])
print(arr.sum(axis=0))
print(arr.mean(axis=1))

# PART C – Broadcasting

# Q6
arr1 = np.array([
    [12, 18, 25],
    [20, 30, 35],
    [15, 22, 28],
    [10, 16, 24]
])

arr2=np.array([5, 10, 15])
print(arr1 + arr2)

# Q7
arr3 = np.array([
    [50, 60, 70],
    [80, 90, 100],
    [110, 120, 130]
])
print(arr3-10)

# PART D – Flatten / Ravel

# Q8

x = np.array([[1,2],
              [3,4],
              [5,6]])
print(x.flatten())
print(x.ravel())
x[0,0]=100
print(x)

# PART E – Sorting & Ranking
# Q9
marks = np.array([72, 88, 65, 90, 78])
print(np.sort(marks))
print((np.argsort(marks)))
print(max(np.argsort(marks)))

# PART F – Statistics & Random Data

# Q10 Generate a 4×4 random integer array between 10 and 50.
arr4 = np.random.randint(10, 51, size=(4, 4))
print(arr4)

# Q11 
print(np.mean(arr4))
print(np.std(arr4,axis=0))
print(np.max(arr4,axis=1))

# 🧠 PART G – Real-World Thinking (Important 🔥)
# Q12
# numpy is the python libary that help to paly with no and mathematical opration a based on array ,
# python list is slow in nature nuppy is fast in nature due to it consist of the from c langauge   

