'''
 Check whether the user input number is even or odd and display it to user
'''
num = int(input("Enter any number: "))
if num/2 == num//2:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

