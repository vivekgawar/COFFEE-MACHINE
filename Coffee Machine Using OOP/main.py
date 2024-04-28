from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_item = MenuItem
menu = Menu()

machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Coffee Machine Closed")
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



