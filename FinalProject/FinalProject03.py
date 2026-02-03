import numpy as np

np.random.seed(10)
data=np.random.randint(20,100 , size=(50,5))
print(data)
print(data.shape)

data[data<40]=40
print(data)

print(np.clip(data,50,95))

Subject_wise_average=np.average(data,axis=0)
print(Subject_wise_average)

Student_wise_total_marks=np.sum(data,axis=1)
print(Student_wise_total_marks)

Identify_top_5_students=np.argsort(Student_wise_total_marks)[-5:][::-1]
print(Identify_top_5_students)

student_wise_average_mark=np.mean(data,axis=1)
print(student_wise_average_mark)
x =(np.where(student_wise_average_mark>=85,"Excelent",
                                    np.where(student_wise_average_mark>=70,"Good","Need To Improve")))
print(x)
