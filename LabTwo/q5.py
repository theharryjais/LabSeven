'''
For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
'''
num = int(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")