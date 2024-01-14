# Using If-else, if-elif-else statements projects shown the real life scenarios
print("\n"+"-"*30+" Welcome to Roller Coaster "+"-"*30+"\n")
height = int(input("What is your height in cm ? : "))

if height >= 120:
    print("\nYou can ride the Roller Coaster")
    age = int(input("\nWhat is your age ? : "))
    if age <= 12:
        bill = 25
        print("\nChild tickets are Rs. 25")
    elif age <= 18:
        bill = 50
        print("\nYouth tickets are Rs. 50")
    else:
        bill = 100
        print("\nAdults tickets are Rs. 100")
        
    wants_photo = input("\nDo you want a photo? Y or N : ")
    if wants_photo == "Y":
        # add Rs. 10 in payment bill
        bill += 10
    print(f"\nYour final bill is {bill}")
else:
    print("\nSorry, you have to grow taller before you can ride")