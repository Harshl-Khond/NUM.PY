

import numpy as np

a=np.random.randint(1,100,size=(8,3))
print(a)


z=np.random.seed(42)
print(z)
print(np.random.randint(1, 10, 5))

marks = np.array([
    [78, 85, 90],
    [88, 76, 92],
    [67, 89, 81],
    [90, 91, 88],
    [72, 80, 75]
])
print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))
print(np.var(marks))


scores = np.array([45, 67, 78, 88, 90, 72, 60])
print(np.percentile(scores, 50)) 
print(np.percentile(scores, 90))
