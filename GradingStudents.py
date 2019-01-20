def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade >= 38:
            if grade % 5 >= 3:
                new_grades.append(grade + (5 - grade % 5) )
            else:
                new_grades.append(grade)
        else:
            new_grades.append(grade)
    return new_grades        




grades = [73, 67, 38, 33]
result = gradingStudents(grades)
print(result)