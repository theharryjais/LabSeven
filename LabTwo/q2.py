'''
2. WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
marks1 = int(input("Enter marks of the first subject: "))
marks2 = int(input("Enter marks of the second subject: "))
marks3 = int(input("Enter marks of the third subject: "))
marks4 = int(input("Enter marks of the fourth subject: "))

avg_marks = (marks1 + marks2 + marks3 + marks4) / 4

if (avg_marks > 70):
    print("You have secured distinction.")
elif (avg_marks > 60):
    print("You have secured first division.")
elif (avg_marks > 40):
    print("You have just passed.")
elif(avg_marks < 40):
    print("You have failed.")