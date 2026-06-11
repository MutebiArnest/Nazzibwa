bill_amount = float(input("Enter total bill amount: "))
no_people = int(input("Enter number of people: "))

print("\nTip Options:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Custom")

tip_choice = int(input("Choose a tip percentage option (1-4): "))
if tip_choice == 1:
    tip_percentage = 10
elif tip_choice == 2:
    tip_percentage = 15
elif tip_choice == 3:
    tip_percentage = 20
elif tip_choice == 4:
    tip_percentage = float(input("Enter custom tip percentage: "))

tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount
amount_per_person = total_bill / no_people

print("\n------Receipt------")
print(f"Bill Amount:        shs{bill_amount:.2f}")
print(f"Tip Percentage:     {tip_percentage}%")
print(f"Tip Amount:         shs{tip_amount:.2f}")
print(f"Total Bill:         shs{total_bill:.2f}")
print(f"Number of People:   {no_people}")
print(f"Amount per Person:  shs{amount_per_person:.2f}")
print("-------------------")