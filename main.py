import pandas as pd
import numpy as np

#Load the student dataset from csv file
students=pd.read_csv("students.csv")
print(students)
print("total students:",len(students))

#selected five subject columns from the dataset
subjects=students[["Python","SQL","HTML","CSS","JavaScript"]]

#calculating total marks using panda
students["Total"]=subjects.sum(axis=1)

#calculate average marks using pandas
students["Average"]=students["Total"]/5

print(students[["Name", "Total","Average"]])

#calculate grade based on average marks
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"
def check_resultS(marks):
    for mark in marks:
        if(mark<40):
            return "Fail"
    
    return "Pass"

#assign grades using the average function
students["Grade"]=students["Average"].apply(assign_grade)

#check pass/fail status using the five subject marks
students["Result"]=students[["Python","SQL","HTML","CSS","JavaScript"]].apply(check_resultS,axis=1)
#display the final analysis of the students dataset
print(students[["Name", "Total", "Average", "Grade", "Result"]])

#Subject-wise performance analysis
print("Subject-wise Average Marks:")
print(subjects.mean())

#NumPy numerical analysis

marks_array = subjects.to_numpy()

print("Highest individual subject mark:", np.max(marks_array))
print("Lowest individual subject mark:", np.min(marks_array))
print("Overall average of all subject marks:", np.mean(marks_array))

# Attendance analysis
print("Average Attendance:", students["Attendance"].mean())

low_attendance = students[students["Attendance"] < 75]

print("Students with attendance below 75%:")
print(low_attendance[["Name", "Attendance"]])

#top 3 students based on average marks
top_students=students.sort_values(by="Average",ascending=False).head(3)

print("Top 3 Students:")
print(top_students[["Name", "Average"]])
