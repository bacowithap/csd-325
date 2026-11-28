# # Francisco Villa           11/27/2026
# Advanced Python           Module 8.2

import json

filename = "Student.json"

def display_students(student_list):
    for student in students:
        print(f"{student['L_Name']}, {student ['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

with open("Student.json", "r", encoding="utf-8") as file:
    students = json.load(file)

print("\nThis is the original Student list")
display_students(students)

added_myself = {
    "F_Name": "Francisco",
    "L_Name": "Villa",
    "Student_ID": 40777,
    "Email": "fmvilla@bellevue.edu"
}
students.append(added_myself)

print("\nThis is the updated Student list")
display_students(students)

with open("Student.json","w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("\nStudent.json File updated")