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
#TODO 1: Initialise the resources with some value
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#TODO 2: Check if the resources are sufficient or not
def is_resource_sufficient(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough

#TODO 3: Print the report of all resources
def resources_print(resources):
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: $ {profit}")
#resources_print(resources)
#TODO 7: Check if transaction is successful
def is_transaction_success(money,cost):
    if money>=cost:
        change=round(money-cost,2)
        print(f"Here is Change: ${change}")
        global profit
        profit+=cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
#TODO 8: Make coffee and deduct the values of resources from the report
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
#TODO 4: Prompt user by asking what they would like to have?
to_continue=True
while(to_continue):
    choice=input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        to_continue=False
    elif choice=='report':
        resources_print(resources)
    else:
        drink=MENU[choice]
        #print(drink)
#TODO 5: Check if the resources are sufficient
        if (is_resource_sufficient(drink['ingredients'])):
#TODO 6: Process the coins
            quarters=int(input("Enter the quarters: "))
            dimes=int(input("Enter the dimes: "))
            nickels=int(input("Enter the nickels: "))
            penny=int(input("Enter the pennies: "))
            monetary_value=quarters*0.25+dimes*0.10+nickels*0.05+penny*0.01
            print(monetary_value)
            if (is_transaction_success(monetary_value,drink['cost'])):
                make_coffee(choice,drink['ingredients'])






