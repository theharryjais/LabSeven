'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''
temp = int(input("What is the temperature?:"))
if temp > 30:
    print("It is a hot day.")
elif temp < 30:
    print("It is a cold day.")
else:
    print("It is neither hot or cold.")


