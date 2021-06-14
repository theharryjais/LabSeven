'''
5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

'''
sectionA = int(input("enter the number of student "))
sectionB=int(input("enter the number of students "))
sectionC=int(input("enter the number of students"))
a= sectionA//2
if sectionA%2==1:
    a=a+1
b= sectionB//2
if sectionB%2==1:
    b=b+1
c= sectionC//2
if sectionC%2==1:
    c=c+1
print(f"the first group has {sectionA} number of students so they require {a} desk ")
print(f"the first group has {sectionB} number of students so they require {b} desk ")
print(f"the first group has {sectionC} number of students so they require {c} desk ")