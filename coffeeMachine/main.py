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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0.0

# TODO Make Coffee


def make_coffee (difference, user_choice):
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    if user_choice != "espresso":
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    print("Here is %.3f in change." % difference)

# TODO Make a function to print the report


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money}")

# TODO Check if the resources available is efficient


def check_resources(drink):
    water_req = MENU[drink]["ingredients"]["water"]
    coffee_req = MENU[drink]["ingredients"]["coffee"]
    if drink == "espresso":
        milk_req = 0
    else:
        milk_req = MENU[drink]["ingredients"]["milk"]
    if water_req > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif coffee_req > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    elif milk_req > resources['milk']:
        print("Sorry there is not enough milk")
    else:
        return True

# TODO Check coins is sufficient


def check_coins(coins, user_choice):
    total_sum = coins['pennies']*0.01 + coins['quarters']*0.25 + coins['dimes']*0.10 + coins['nickels']*0.05
    if total_sum >= MENU[user_choice]["cost"]:
        difference = total_sum - MENU[user_choice]["cost"]
        make_coffee(difference, user_choice)
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded: ${total_sum}")
        return False


# TODO Take in the coins!!!


def take_coins(user_choice):
    coins = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0,
    }
    for i in coins:
        coins[i] = int(input(f"How many {i}? "))
    sufficient = check_coins(coins, user_choice)
    if sufficient:
        return True
    else:
        return False

# TODO Prompt the user to what he/she wants


todo = True
while todo:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if type(user_choice) == str:
        if user_choice == "off":
            todo = False
        elif user_choice == "report":
            print_report()
        elif user_choice in MENU:
            check = check_resources(user_choice)
            if check:
                print("Please Insert Coins")
                sufficient_coins = take_coins(user_choice)
                if sufficient_coins:
                    total_money += MENU[user_choice]["cost"]
                    print(f"Here is your {user_choice} ☕")
        else:
            print("Invalid Input!")