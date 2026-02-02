import numpy as np

# Generate a 30×5 dataset (scores 40–100)

np.random.seed(10)
scores=np.random.randint(40,100 , size=(30,5))
print(scores)

# Replace scores < 50 with 50
scores[scores<50]=50
print(scores)

# Cap scores > 95 at 95
print(np.clip(scores,50,95))

x=np.sum(scores,axis=1)
print(x)
employee=(np.where(scores>=85,"Excellent",
                   np.where(scores>=70,"Good","need Improve")))
print(employee)
