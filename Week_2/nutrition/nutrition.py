def main():
    item = input("Item: ").lower()
    print(f"Calories: {calories(item)}")

def calories(item):
    fruts = [
        {"name": "apple", "calories": 130},
        {"name": "banana", "calories": 110},
        {"name": "orange", "calories": 85},
        {"name": "grape", "calories": 75},
        {"name": "pear", "calories": 100},
        {"name": "strawberry", "calories": 95},
        {"name": "blueberry", "calories": 105},
        {"name": "raspberry", "calories": 85},
        {"name": "blackberry", "calories": 75},
        {"name": "cranberry", "calories": 105},
        {"name": "kiwifruit", "calories": 90},
        {"name": "mango", "calories": 105},
        {"name": "pineapple", "calories": 85},
        {"name": "papaya", "calories": 75},
        {"name": "avocado", "calories": 50},
        {"name": "peach", "calories": 95},
        {"name": "cherry", "calories": 105},
        {"name": "plum", "calories": 85},
        {"name": "blackcurrant", "calories": 75},
        {"name": "coconut", "calories": 105},
        {"name": "clementine", "calories": 95},
        {"name": "dragonfruit", "calories": 105},
        {"name": "durian", "calories": 85},
        {"name": "sweet cherries", "calories": 100},
    ]

    for fruit in fruts:
        if item == fruit["name"]:
            return fruit["calories"]
    exit()
main()