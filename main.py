MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
machine_on = True
coins = 0


# TODO 5: Process coins
def process_coins():
    global coins
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


# TODO 6: Check transaction successful?
def check_transaction():
    global coins, money
    if coins < MENU[coffe_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        money += MENU[coffe_type]['cost']
        if coins > MENU[coffe_type]['cost']:
            change = coins - MENU[coffe_type]['cost']
            print(f"Here is ${round(change, 2)} dollars in change.")


# TODO 7: Make coffe
def make_coffee():
    resources['water'] -= MENU[coffe_type]['ingredients']['water']
    resources['milk'] -= MENU[coffe_type]['ingredients']['milk']
    resources['coffee'] -= MENU[coffe_type]['ingredients']['coffee']
    print(f"Here is your {coffe_type} ☕. Enjoy!")


while machine_on:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
    coffe_type = input("What would you like? (espresso/latte/cappuccino):")
    # TODO 2: Turn off the machine by entering "off" to the prompt

    if coffe_type == "off":
        machine_on = False

    # TODO 3: Print report
    elif coffe_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${money}")

    # TODO 4: Check resources sufficient?
    else:
        if MENU[coffe_type]['ingredients']['water'] <= resources['water']:
            if MENU[coffe_type]['ingredients']['milk'] <= resources['milk']:
                if MENU[coffe_type]['ingredients']['coffee'] <= resources['coffee']:
                    process_coins()
                    check_transaction()
                    if coins >= MENU[coffe_type]['cost']:
                        make_coffee()
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")
