
from menu import menu

def save_receipt(order, total):
    with open("bills.txt", "a") as file:
        file.write("\n========== CANTEEN RECEIPT ==========\n")

        for item_no, quantity in order.items():
            name, price = menu[item_no]
            amount = price * quantity
            file.write(f"{name} x {quantity} = Rs. {amount}\n")

        file.write(f"Total Amount: Rs. {total}\n")
        file.write("=====================================\n")

    print("Receipt saved successfully!")
