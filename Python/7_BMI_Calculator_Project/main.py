height = input("\nEnter your height : ")
weight = input("\nEnter your weight : ")
bmi = int(weight) / float(height) ** 2
print(f"\nYour BMI is : {bmi}")
bmi_in_int = int(bmi)
print(f"\nYour BMI score is : {bmi_in_int}")