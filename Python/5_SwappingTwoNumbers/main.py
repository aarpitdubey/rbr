number_1 = int(input("Enter the first number  : "))
number_2 = int(input("Enter the second number : "))

# With the temporary/extra variable
temp     = number_1
number_1 = number_2
number_2 = temp

print(f"First number value becomes : {number_1}" \
      f"\nSecond number value becomes : {number_2}")