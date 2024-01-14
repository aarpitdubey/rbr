# If the bill was Rs. 150, split between 5 people, with 12% tip.
# Each people shoiuld pay (150.0 / 5) * 1.12 = 33.6
# Round the result to decimal places = 33.60

print("\n"+"-"*30+" Welcome to the bill calculator "+"-"*30+"\n")

bill = float(input("What was the bill? Rs. :  "))
tip = int(input("\nHow much percent of tip would like to pay 10, 15, 20 : "))
people = int(input("\nHow many people to split the bill : "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"\nTotal Bill per person : {final_amount}")

