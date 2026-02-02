import numpy as np

arr = np.array([25, 45, 60, 75, 90])
print(np.where(arr>=60,"good","Bad"))

scores = np.array([30, 55, 110, 85, 45])
print(np.clip(scores,50,100))

x = np.array([4, 9, 16, 25])
print(np.sqrt(x))