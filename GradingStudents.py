def gradingStudents(grades):
    newGrades=[]
    for grade in grades:
        rem=grade%5
        diff=5-rem
        if grade>=38 and diff<3:
            grade+=diff
        newGrades.append(grade)
    return print(newGrades)
gradingStudents([45,29,98,67,57])            
