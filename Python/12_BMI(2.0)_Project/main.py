height = float(input("\nEnter your height in m  : "))
weight = float(input("\nEnter your weight in kg : "))
bmi    = round(weight / height ** 2)

if bmi < 18.5:
    print(f"\nYour bmi is {bmi}, You are under weight.")
elif bmi < 25:
    print(f"\nYour bmi {bmi}, You are normal weight.")
elif bmi < 30:
    print(f"\nYour bmi {bmi}, You are overweight.")
elif bmi < 35:
    print(f"\nYour bmi {bmi}, You are obese.")
else:
    print(f"\nYour bmi {bmi}, You are clinically obese.")