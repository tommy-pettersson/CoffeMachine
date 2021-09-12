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


def is_resources_sufficient(order_ingredients):
    """This function return True if the machines resources is enough for the selected drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True


def process_coins():
    """This function returns the total value of the coins added to the machine."""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_payment_sufficient(amount_paid, drink_cost):
    """This function returns True if the payment is sufficient for the selected drink."""
    if amount_paid >= drink_cost:
        global profit
        profit += drink_cost
        if amount_paid > drink_cost:
            change = round(amount_paid - drink_cost, 2)
            print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry, not enough money. Money is refunded.")
        return False


def make_coffee(order_ingredients):
    """The purpose of this function is to deduct resources from the machine when a coffee is made."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_sufficient(payment, drink["cost"]):
                make_coffee(drink["ingredients"])
