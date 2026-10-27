
menu = {
    1: ("Tea", 10),
    2: ("Coffee", 20),
    3: ("Samosa", 15),
    4: ("Sandwich", 40),
    5: ("Poha", 25),
    6: ("Vadapav", 20)
}


def display_menu():
    print("\n========== CANTEEN MENU ==========")
    print(f"{'No.':<8}{'Food Item':<15}{'Price':>8}")
    print("----------------------------------")

    for number, item in menu.items():
        print(f"{number:<8}{item[0]:<15}₹{item[1]:>6}")

    print("==================================")
