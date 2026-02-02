import numpy as np

arr=np.array([1,8,7,5,6,9,3,5,6])
print(arr)
print(arr[arr>5])
print(arr[(arr>4) & (arr<8)])

marks = np.array([
    [78, 85, 90],
    [88, 76, 92],
    [67, 89, 81],
    [90, 91, 88]
])

print(marks[marks<80])
marks[marks<80]=30
print(marks)

arr1=np.array([4,5,7,2,3,7,9])
index=[1,3,5]
print(arr1[index])