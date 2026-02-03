# DATASET 2: Course Sales
import numpy as np

np.random.seed(10)
sales=np.random.randint(100,5000, size=(20, 30))
print(sales)
print(sales.shape)

course_wise_total=np.sum(sales,axis=1)
print(course_wise_total)

# Best selling course (overall)
print(np.argmax(course_wise_total))

# Worst selling course
print(np.argmin(course_wise_total))

# Apply discount:
# If daily average < ₹2000 → apply 15% discount

daily_avg=np.mean(sales,axis=0)
print(daily_avg)
discount_days = np.where(daily_avg < 2000, "15% Discount", "No Discount")
print(discount_days)

