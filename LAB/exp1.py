import numpy as np

student_scores = np.loadtxt("Students_data.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

highest_subject = subjects[np.argmax(average_scores)]

print("Average scores:", np.round(average_scores, 2))
print("Subject with highest average score:", highest_subject)
