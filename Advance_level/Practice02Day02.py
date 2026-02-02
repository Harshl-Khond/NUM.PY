import numpy as np

arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
print(np.log(arr))
print(np.exp(arr)) 

arr1 = np.array([40, 65, 80, 55, 90])

result = np.where(arr1 >= 60, "Pass", "Fail")
print(result)

marks = np.array([35, 50, 78, 95, 110,120])

print(np.clip(marks, 40, 100))


data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.apply_along_axis(np.mean, axis=1, arr=data))
