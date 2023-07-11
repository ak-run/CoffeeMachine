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

coffee_choices = MENU.keys()

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# our coffee machine is on by default and lets the while loop run
is_on = True


def print_report():
    """function to print report of resources and profit"""
    for key, value in resources.items():
        print(f"{key}: {value}")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, false if ingredients insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    else:
        return True


# TODO: Update resources

def update_resources(drink_purchased):
    """Updates resources and profit after drink is purchased by deducting required ingredients from resources"""
    req_ingredients = MENU[drink_purchased]["ingredients"]
    for key, value in req_ingredients.items():
        resources[key] -= value
    global profit
    profit = profit + MENU[choice]["cost"]


def coin_payment(drink_chosen):
    """Return True if payment take, False if not enough coins"""
    cost_of_drink = MENU[drink_chosen]["cost"]
    total = int(input("number of quarters: ")) * 0.25
    total += int(input("number of dimes: ")) * 0.1
    total += int(input("number of nickles: ")) * 0.05
    total += int(input("number of pennies: ")) * 0.01
    if total >= cost_of_drink:
        change = round(total - cost_of_drink, 2)
        print(f"Here's ${change} change for you.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def making_coffee(chosen_drink):
    print(f"Here's your ☕️ {chosen_drink}. Enjoy!")


while is_on:
    # Prompt user to choose their drink
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the machine by entering "off" prompt
    if choice == "off":
        is_on = False
    # if report is chosen it prints resources and profit
    elif choice == "report":
        print_report()
    elif choice in coffee_choices:
        """Check transaction successful (both coins and resources)"""
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            if coin_payment(choice):
                update_resources(choice)
                making_coffee(choice)
    # in case user inputs outside of menu or other options
    else:
        print("This product doesn't exist. Start over.")
