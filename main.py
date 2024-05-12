#Anoushka Saha
#OOP Coffee Machine
#May 12th, 2024
#Day 16 Final Project

#Importing
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    #Ask user for order
    order = input(f"What would you like? ({menu.get_items()}): ")

    #Report printing function
    if order == "off":
        exit()
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order) 
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

