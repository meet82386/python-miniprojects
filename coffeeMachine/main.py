MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300.0,
    "milk": 200.0,
    "coffee": 100.0,
    "money": 100.0
}


def enough_resources(coffee):
    """Functions checks if enough resources are available or not."""
    required = MENU.get(coffee).get("ingredients")

    for item, amount in required.items():
        if resources.get(item) < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def money_count(coffee):
    """Collects money from user and checks if amount is sufficient to make coffee. Also returns change."""
    pennies = float(input("Enter number of pennies: "))
    nickels = float(input("Enter number of nickels: "))
    dimes = float(input("Enter number of dimes: "))
    quarters = float(input("Enter number of quarters: "))

    total_value = (0.01 * pennies) + (0.05 * nickels) + (0.1 * dimes) + (0.25 * quarters)
    required_value = MENU.get(coffee).get("cost")
    difference = total_value - required_value

    if difference < 0:
        print("No enough money to get coffee. ")
        print(f"You have entered {round(required_value - total_value, 2)} less.")
        return False

    if difference > resources.get('money'):
        print("We are running out of change, sorry.")
        return False

    resources['money'] = resources.get('money') + required_value

    if difference != 0:
        print(f"Wait for {coffee} on your table, Here is your ${round(difference, 2)} change")
    return True


def make_coffee(coffee):
    """Makes coffee using available resources"""
    for item, amount in MENU.get(coffee).get("ingredients").items():
        resources[item] = resources.get(item) - amount


while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    valid_inputs = ["espresso", "latte", "cappuccino", "off", "report"]

    if coffee_type not in valid_inputs:
        print("Invalid input.")
        continue

    if coffee_type in valid_inputs[:3]:
        if not enough_resources(coffee_type) or not money_count(coffee_type):
            continue
        make_coffee(coffee_type)

    if coffee_type == "off":
        break

    if coffee_type == "report":
        print(f"Water: {resources.get('water')}ml")
        print(f"Milk: {resources.get('milk')}ml")
        print(f"Coffee: {resources.get('coffee')}g")
        print(f"Money: ${resources.get('money')}")
