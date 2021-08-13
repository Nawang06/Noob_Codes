from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_continue = True

items = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

while is_continue:
    item_name = input(f"What would you like to have? {items.get_items()}: ")
    if item_name == "report":
        coffee.report()
        money.report()
    elif item_name == "off":
        is_continue = False
    else:
        item_details = items.find_drink(item_name)
        if item_details:
            resources_check = coffee.is_resource_sufficient(item_details)
            if resources_check:
                payment_result = money.make_payment(item_details.cost)
                if payment_result:
                    coffee.make_coffee(item_details)


