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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_sufficient(order_ingredients):                   # Check available resources
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'report':                          # Print Report
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: {profit}")

    elif choice == 'off':
        break
    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            total = process_coins()                 # Get total $ given by user
            if total >= drink["cost"]:
                temp_ingredients = drink["ingredients"]
                profit += drink["cost"]             # Update Profit
                # Update Resources
                resources["water"] -= temp_ingredients["water"]
                if choice != "espresso":
                    resources["milk"] -= temp_ingredients["milk"]
                resources["coffee"] -= temp_ingredients["coffee"]
                # Calculate change and give it back to user
                change = round(total - drink["cost"], 2)
                print(f"\nHere is ${change} dollars in change.")

                print(f"Here is your {choice} ☕️Enjoy!")

            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
