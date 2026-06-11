username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    role = "admin"
elif username == "customer" and password == "cust123":
    role = "customer"
elif username == "cashier" and password == "cash123":
    role = "cashier"
else:
    print("Invalid username or password")
    exit()

print(f"Welcome {username}!")
print(f"Your role is: {role}")


if role == "Admin":
    print("Access Level: Full access to all features")
elif role == "Cashier":
    print("Access Level: Process sales and payments")
elif role == "Customer":
    print("Access Level: View and purchase products")

subtotal = float(input("Enter product subtotal: "))
if subtotal >= 500000:
    discount_percent = 20
elif subtotal >= 200000:
    discount_percent = 10
elif subtotal >= 100000:
    discount_percent = 5
else:
    discount_percent = 0

coupon = input("Enter coupon code (SAVE10, SAVE20) or press Enter: ")
if coupon  != "":
    if coupon == "SAVE10":
        discount_percent += 10
    elif coupon == "SAVE20":
        discount_percent += 20
    else:
        print("Invalid coupon code")

discount_amount = subtotal * discount_percent / 100
amount_after_discount = subtotal - discount_amount

location = input("Enter location (Kampala, Wakiso, Mukono): ")
if location.lower() == "kampala":
    tax_rate = 18
elif location.lower() == "wakiso":
    tax_rate = 15 
elif location.lower() == "mukono":
    tax_rate = 12
else:
    tax_rate = 10
tax_amount = amount_after_discount * tax_rate / 100
final_price = amount_after_discount + tax_amount

print("\n------- Receipt -------")
print(f"Subtotal: {subtotal:,.0f}")
print(f"Discount Applied: {discount_percent}%")
print(f"Discount Amount: {discount_amount:,.0f}")
print(f"Amount After Discount: {amount_after_discount:,.0f}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: {tax_amount:,.0f}")
print(f"Final Price: {final_price:,.0f}")
print("Thank you for shopping with us!")
print("-----------------")