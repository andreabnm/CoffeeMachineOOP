from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True
menu = Menu()
maker = CoffeeMaker()
moneyMachine = MoneyMachine()

while isOn:
    options = menu.get_items()
    userChoice = input(f'What would you like? ({options}): ')

    if userChoice == 'off':
        isOn = False
    elif userChoice == 'report':
        maker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(userChoice)
        if maker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                maker.make_coffee(drink)


