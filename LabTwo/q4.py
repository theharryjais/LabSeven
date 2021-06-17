'''
Given three integers, print the smallest one. (Three integers should be user input)
'''
a=int(input('Enter a no'))
b=int(input('Enter a no'))
c=int(input('Enter a no'))
small=a
list=(a,b,c)
for i in list:
    if i<=small:
        small=i
print (f'Smallest no is {small}')