name = input("enter your name:")
age = int(input("enter the age:"))

print("Hello my nme is" +name+ "and i am"+str(age)+"years old")
print("Hello my nme is", name, "and i am",age,"years old")
print("Hello my nme is %s and i am %d years old"% (name,age,))
print("Hello my nme is {} and i am {} years old". format (name,age,))
print(f"Hello my nme is {name}and i am {age} years old")