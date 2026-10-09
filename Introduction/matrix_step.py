import numpy as np

# A 2D Matrix: 3 students (rows), 4 exam scores each (columns)
grades = np.array([
    [80, 85, 90, 95],
    [70, 75, 80, 85],
    [90, 92, 88, 94]
])

# 1. Shape Inspection
print("Matrix Shape:", grades.shape)

# 2. Row/Column Slicing
student_1_scores = grades[0, :]
exam_2_scores = grades[:, 1]

print("Student 1 (Row 0):", student_1_scores)
print("Exam 2 Scores (Column 1):", exam_2_scores)

# 3. Axis-Based Reductions
class_exam_means = np.mean(grades, axis=0)
student_averages = np.mean(grades, axis=1)

print("Average per Exam (across rows):", class_exam_means)
print("Average per Student (across columns):", student_averages)
