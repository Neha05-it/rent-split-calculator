## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Change per unit
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered ="))
electricity_spend = int(input("Enter the total of electricity spend = "))
persons = int(input("Enter the number of persons living in room/flat = "))

output = (food + rent + electricity_spend) // persons

print("Each person will pay = ", output)
