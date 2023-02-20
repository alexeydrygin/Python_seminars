

import os

STUDENTS_FILE = 'students.txt'
GRADES_FILE = 'grades.txt'

def add_student(name, surname, patronymic, birth_date, grade, address, phone_number):
    with open(STUDENTS_FILE, 'a', encoding="utf-8") as file:
        file.write(f"{name},{surname},{patronymic},{birth_date},{grade},{address},{phone_number}\n")

def delete_student(surname):
    with open(STUDENTS_FILE, 'r', encoding="utf-8") as file:
        students = file.readlines()
    with open(STUDENTS_FILE, 'w', encoding="utf-8") as file:
        for student in students:
            if student.split(',')[1] != surname:
                file.write(student)

def add_grade(student_id, subject, grade):
    with open(GRADES_FILE, 'a', encoding="utf-8") as file:
        file.write(f"{student_id},{subject},{grade}\n")

def get_grades(surname):
    with open(STUDENTS_FILE, 'r', encoding="utf-8") as file:
        students = file.readlines()
    with open(GRADES_FILE, 'r', encoding="utf-8") as file:
        grades = file.readlines()
    student_id = None
    for student in students:
        if student.split(',')[1] == surname:
            student_id = student.split(',')[0]
            break
    if student_id:
        student_grades = []
        for grade in grades:
            if grade.split(',')[0] == student_id:
                subject = grade.split(',')[1]
                grade_value = int(grade.split(',')[2])
                student_grades.append((subject, grade_value))
        return student_grades
    else:
        return []
