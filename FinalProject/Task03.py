import numpy as np

# Generate 20×15 dataset

np.random.seed(10)
scores=np.random.randint(1,9 , size=(20,15))
print(scores)

# Find:
# Best selling product
# Worst selling product

total=np.sum(scores,axis=1)
print(total)

# Best selling product
Best_selling=np.argmax(total)
print(Best_selling)

# Worst selling product
wrost_selling=np.argmin(total)
print(wrost_selling)

# Daily average sales

daily_avg=np.mean(scores,axis=0)
print(daily_avg)


discount = np.where(daily_avg < 4, "10% Discount", "No Discount")
print(discount)







