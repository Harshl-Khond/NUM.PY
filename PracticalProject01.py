import numpy as np

marks=np.array([[78, 85, 90],[88, 76, 92], [67, 89, 81],[90, 91, 88],[72, 80, 75]])
print(marks.shape)
print(marks.size)
print(marks.dtype)

subject_avg = np.mean(marks, axis=0)
print("Subject-wise Average:", subject_avg)

subject_max=np.max(marks,axis=0)
print(subject_max)

subject_min=np.min(marks,axis=0)
print(subject_min)


total_marks_per_student = np.sum(marks,axis=1)
print("Total Marks per Student:", total_marks_per_student)

avg_mark_per_student=np.average(marks,axis=1)
print("Average Marks per Student:", avg_mark_per_student)

top_scoring_student = np.max(marks,axis=1)
print("Top Scoring Student Marks:", top_scoring_student)

print("Marks of Student 3:", marks[2])
print("English marks:", marks[:, 2])
print("First 3 students marks:\n", marks[:3])

math_scores = marks[:, 0]
students_above_85 = math_scores > 85

print("Math scores:", math_scores)
print("Students scoring >85 in Math:", students_above_85)

marks[marks < 75] = 75
print("Updated marks after grace:\n", marks)


# Which subject is hardest (lowest average)?
# Math is the hardest subject because it has the lowest average marks compared to Science and English.


# How NumPy made this easier compared to Python lists?
# NumPy allows vectorized operations, slicing, and condition-based filtering without writing loops, making the code shorter, faster, and cleaner than Python lists


