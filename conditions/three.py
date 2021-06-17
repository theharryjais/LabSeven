'''
Weight
'''
unit = input("enter unit (kg/lbs):").lower()
weight = int(input("enter your weight:"))
if unit=='kg':
    converted_weight = weight*2.20462
    print(f"your weight is {converted_weight}lbs.")
elif unit == "lbs":
        converted_weight = weight * 0.453592
        print(f"Your weight is {converted_weight} kg.")
else:
      print("Use either 'kg' or 'lbs' as unit.")