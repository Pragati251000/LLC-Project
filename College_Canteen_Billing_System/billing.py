
from menu import menu

def place_order():
    order = {}

    while True:
        print("\nEnter item number to order (0 to finish)")
        item_no = int(input("Item number: "))

        if item_no == 0:
            break

        if item_no in menu:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                order[item_no] = order.get(item_no, 0) + quantity
                print("Item added successfully!")
            else:
                print("Quantity must be greater than zero.")
        else:
            print("Invalid item number!")

    return order

def calculate_bill(order):
    from menu import menu

    total = 0

    print("\n========== BILL ==========")
    print("Food Item    Qty    Price    Amount")

    for item_no, quantity in order.itsems():
        name, price = menu[item_no]
        amount = price * quantity
        total += amount

        print(name, "   ", quantity, "   ₹", price, "   ₹", amount)

    print("--------------------------")
    print("Total Amount: ₹", total)
    print("==========================")

    return total

