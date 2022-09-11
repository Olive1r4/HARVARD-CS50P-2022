def main():
    get_price()

def get_price():
    total = 0
    # An array of lists
    products = [
        {"name": "Baja Taco", "price": 4.00},
        {"name": "Burrito", "price": 7.50},
        {"name": "Bowl", "price": 8.50},
        {"name": "Nachos", "price": 11.00},
        {"name": "Quesadilla", "price": 8.50},
        {"name": "Super Burrito", "price": 8.50},
        {"name": "Super Quesadilla", "price": 9.50},
        {"name": "Taco", "price": 3.00},
        {"name": "Tortilla Salad", "price": 8.00},
    ]

    while True:
        try:
            item = input("Item: ").title()
            for product in products:
                if item == product["name"]:
                    total += product["price"]
                    print(f"Total: ${total:.2f}")
        # If user end input(ex. control+d) without reading any data the method will return an empty string
        except EOFError:
            print()
            break
        # If user input is not an item in the list
        except KeyError:
            pass
main()