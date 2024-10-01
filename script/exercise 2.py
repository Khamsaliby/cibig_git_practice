# ask the user to enter 3 grades, which are stored in 3 variables
grade1 = input("Enter first grade: ")
grade2 = input("Enter second grade: ")
grade3 = input("Enter third grade: ")

#all grades list
grades_list = [grade1,grade2,grade3]
print(grades_list)
print(grades_list[0])
print(len(grades_list))


#grade total
grades_total = float(grade1) + float(grade2) + float(grade3)
#print(grades_total)

#calculate average of all grades
average_grades = grades_total / 3
print(average_grades)

## IF exer (elif)
# "failed" if the average is less than 10
# "passable" if the average is greater than or equal to 10
# "fairly good" if the average is greater than or equal to 12
# "good" if the average is greater than or equal to 14
# "very good" if the average is greater than or equal to 16


if average_grades < 10:
    grade = "failed"
elif 10 <= average_grades < 12:
    grade = "passable"
elif 12 <= average_grades < 14:
    grade = "fairly good"
elif 14 <= average_grades < 16:
    grade = "good"
elif average_grades > 16 :
    grade = "very good"
else :
    grade = "Error"

print(grade)

###################################################
#LISTS


