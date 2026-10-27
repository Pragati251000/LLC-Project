
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

menu = {
    "South Indian": {
        "Masala Dosa": 60,
        "Idli Sambar": 40,
        "Medu Vada": 35,
        "Plain Dosa": 40,
        "Uttapam": 50,
        "Mysore Dosa": 65
    },
    "Manchurian & Chinese": {
        "Veg Manchurian": 70,
        "Gobi Manchurian": 80,
        "Paneer Chilli": 100,
        "Veg Hakka Noodles": 70,
        "Schezwan Noodles": 80,
        "Veg Fried Rice": 75
    },
    "Drinks": {
        "Tea": 15,
        "Coffee": 25,
        "Cold Coffee": 50,
        "Lemon Juice": 25,
        "Orange Juice": 40,
        "Mango Milkshake": 60
    },
    "Snacks & Fast Food": {
        "Cheese Sandwich": 60,
        "Veg Burger": 50,
        "Cheese Nachos": 70,
        "Veg Pizza": 100,
        "French Fries": 50,
        "Samosa": 15
    }
}


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>College Canteen</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #fff8ef;
                color: #333;
                text-align: center;
            }
            header {
                background: #7b2d26;
                color: white;
                padding: 25px;
            }
            header h1 {
                margin: 0;
                font-size: 34px;
            }
            .hero {
                padding: 75px 20px;
            }
            .hero h2 {
                color: #7b2d26;
                font-size: 32px;
            }
            .hero p {
                font-size: 18px;
                color: #666;
            }
            .btn {
                display: inline-block;
                background: #e67e22;
                color: white;
                padding: 14px 30px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                margin-top: 20px;
            }
            .btn:hover {
                background: #c76512;
            }
            footer {
                padding: 20px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>College Canteen</h1>
            <p>Fresh Food, Happy Mood!</p>
        </header>

        <div class="hero">
            <h2>Welcome to Our Canteen</h2>
            <p>Delicious food and refreshing drinks at affordable prices.</p>
            <p>Choose your favourites and generate your bill online.</p>
            <a class="btn" href="/menu">Explore Menu</a>
        </div>

        <footer>College Canteen Billing System | Python Mini Project</footer>
    </body>
    </html>
    """


@app.route("/menu", methods=["GET", "POST"])
def show_menu():
    if request.method == "POST":
        order = []
        total = 0

        for category, items in menu.items():
            for item, price in items.items():
                try:
                    quantity = int(request.form.get(item, 0))
                except (ValueError, TypeError):
                    quantity = 0

                quantity = max(0, min(quantity, 50))

                if quantity > 0:
                    amount = price * quantity
                    total += amount
                    order.append((item, quantity, price, amount))

        if not order:
            return """
            <html>
            <body style="font-family:Arial;text-align:center;padding:50px">
                <h2>Please select at least one food item.</h2>
                <a href="/menu">Return to Menu</a>
            </body>
            </html>
            """

        receipt_number = datetime.now().strftime("%Y%m%d%H%M%S")
        date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        receipt_rows = ""

        for item, quantity, price, amount in order:
            receipt_rows += f"""
            <tr>
                <td>{item}</td>
                <td>{quantity}</td>
                <td>Rs. {price}</td>
                <td>Rs. {amount}</td>
            </tr>
            """

        receipt = f"""
        <html>
        <head>
            <title>Canteen Receipt</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #fff8ef;
                    text-align: center;
                    padding: 25px;
                }}
                .receipt {{
                    max-width: 750px;
                    margin: auto;
                    background: white;
                    padding: 25px;
                    border-radius: 12px;
                    box-shadow: 0 3px 12px #ddd;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 25px;
                }}
                th, td {{
                    padding: 12px 6px;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background: #7b2d26;
                    color: white;
                }}
                .total {{
                    color: #7b2d26;
                    font-size: 25px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 12px 22px;
                    margin: 10px;
                    border-radius: 6px;
                    text-decoration: none;
                    border: none;
                    cursor: pointer;
                    background: #e67e22;
                    color: white;
                }}
                @media print {{
                    .no-print {{ display: none; }}
                    body {{ background: white; padding: 0; }}
                    .receipt {{ box-shadow: none; }}
                }}
            </style>
        </head>
        <body>
            <div class="receipt">
                <h1>College Canteen</h1>
                <h3>Order Receipt</h3>
                <p>Receipt No: {receipt_number}</p>
                <p>Date: {date_time}</p>

                <table>
                    <tr>
                        <th>Item</th>
                        <th>Qty</th>
                        <th>Price</th>
                        <th>Amount</th>
                    </tr>
                    {receipt_rows}
                </table>

                <h2 class="total">Total: Rs. {total}</h2>

                <div class="no-print">
                    <button class="btn" onclick="window.print()">
                        Print Receipt
                    </button>
                    <a class="btn" href="/menu">Order Again</a>
                    <a class="btn" href="/">Home</a>
                </div>
            </div>
        </body>
        </html>
        """

        with open("bills.txt", "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 40 + "\n")
            file.write("COLLEGE CANTEEN RECEIPT\n")
            file.write(f"Receipt No: {receipt_number}\n")
            file.write(f"Date: {date_time}\n")

            for item, quantity, price, amount in order:
                file.write(
                    f"{item} x {quantity} = Rs. {amount}\n"
                )

            file.write(f"Total Amount: Rs. {total}\n")
            file.write("=" * 40 + "\n")

        return receipt

    sections = ""

    for category, items in menu.items():
        cards = ""

        for item, price in items.items():
            cards += f"""
            <div class="food-card">
                <div class="food-name">{item}</div>
                <div class="price">Rs. {price}</div>
                <label for="item_{item}">Quantity</label>
                <input
                    type="number"
                    id="item_{item}"
                    name="{item}"
                    form="orderform"
                    min="0"
                    max="50"
                    value="0">
            </div>
            """

        sections += f"""
        <section class="category">
            <h2>{category}</h2>
            <div class="food-grid">
                {cards}
            </div>
        </section>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Canteen Menu</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #fff8ef;
                color: #333;
            }}
            header {{
                background: #7b2d26;
                color: white;
                padding: 22px;
                text-align: center;
            }}
            header h1 {{
                margin: 0;
            }}
            .intro {{
                text-align: center;
                padding: 15px;
            }}
            .category {{
                max-width: 1100px;
                margin: 25px auto;
                padding: 0 20px;
            }}
            .category h2 {{
                color: #7b2d26;
                border-bottom: 3px solid #e67e22;
                padding-bottom: 10px;
            }}
            .food-grid {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 18px;
            }}
            .food-card {{
                background: white;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 3px 10px #e8ded3;
            }}
            .food-name {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
            .price {{
                color: #b45309;
                font-size: 17px;
                margin-bottom: 15px;
            }}
            input[type=number] {{
                width: 70px;
                padding: 8px;
                margin-left: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            .actions {{
                text-align: center;
                padding: 25px;
            }}
            .btn {{
                display: inline-block;
                background: #e67e22;
                color: white;
                border: none;
                padding: 14px 28px;
                border-radius: 7px;
                text-decoration: none;
                font-size: 16px;
                cursor: pointer;
                margin: 8px;
            }}
            .btn:hover {{
                background: #c76512;
            }}
            .home-link {{
                display: inline-block;
                color: #7b2d26;
                margin: 10px;
            }}
            footer {{
                background: #7b2d26;
                color: white;
                text-align: center;
                padding: 18px;
            }}
            @media (max-width: 700px) {{
                .food-grid {{
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }}
            }}
            @media (max-width: 450px) {{
                .food-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Our Food Menu</h1>
            <p>College Canteen Billing System</p>
        </header>

        <div class="intro">
            <h2>Choose Your Favourite Food</h2>
            <p>Select quantities and generate your bill.</p>
        </div>

        <form id="orderform" method="POST">
            {sections}
            <div class="actions">
                <button class="btn" type="submit">Generate Bill</button>
                <a class="home-link" href="/">Back to Home</a>
            </div>
        </form>

        <footer>Fresh Food, Happy Mood!</footer>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5055)
