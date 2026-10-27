
from menu import display_menu
from billing import place_order, calculate_bill
from receipt import save_receipt


print("================================")
print("   COLLEGE CANTEEN BILLING SYSTEM")
print("================================")

order = {}

while True:
    print("\n1. View Menu")
    print("2. Place Order")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()

    elif choice == "2":
        display_menu()
        order = place_order()
        print("Order recorded successfully!")

    
    elif choice == "3":
        if order:
          total = calculate_bill(order)
          save_receipt(order, total)
        else:
          print("Please place an order first.")

    elif choice == "4":
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice. Please try again.")
