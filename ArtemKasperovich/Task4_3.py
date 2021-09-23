# ### Task 4.3
# File `data/students.csv` stores information about students in
# [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students


# 2) Implement a function which receives the file path with srudents info and writes CSV student information
# to the new file in descending order of age.


import csv


def get_top_performers(file_path, number_of_top_students=5):
    """
    Receive file path and return names of top performer students
    """
    with open(file_path) as students:
        students = list(csv.DictReader(students))
        lst = sorted(students, key=lambda row: float(row['average mark']), reverse=True)
        print(*lst[:number_of_top_students], sep='\n')


def sorted_by_age(file_path):
    """
    Receive file path with students info and writes new CSV student information
    to the new CSV-file in descending order of age
    """
    with open(file_path) as students:
        with open('./students_sorted_by_age.csv', 'w') as result:
            students = list(csv.DictReader(students))
            sorted_stud = sorted(students, key=lambda row: row['age'], reverse=True)
            columns = [
                'student name',
                'age',
                'average mark'
            ]
            writer = csv.DictWriter(result, fieldnames=columns)
            writer.writerows(sorted_stud)
