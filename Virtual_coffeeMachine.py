MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
    "dollar": 0,
}


def change(amount):
    print("Please Insert a Coin")
    nquarters = int(input("How many quarters?"))
    ndimes = int(input("How many dimes?"))
    nnickles = int(input("How many nickles?"))
    npennies = int(input("How many pennies?"))
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    total = quarters*nquarters+dimes*ndimes+nnickles*nickles+npennies*pennies
    if total >= amount:
        change_amount = total-amount
        print (f"Your Change is {change_amount}")
        resources["dollar"]=resources["dollar"]+amount
        ingredient(amount)
    elif amount>total:
        print("Less Money Given")

def make(amount):
    if amount == 1.50:
        dish = "espresso"
    elif amount == 2.50:
        dish == "latte"
    elif amount == 3.00:
        dish == "cappuccino"
    if resources["water"]>MENU[dish]["ingredients"]['water']:
        if resources["milk"]>MENU[dish]["ingredients"]['milk']:
            if resources["coffee"]>MENU[dish]["ingredients"]['coffee']:
                change(amount)
            else:
                print("Not Enough Coffee")
        else:
            print("Not Enough Milk")
    else:
        print("Not enough Water")
    
def ingredient(amount):
    if amount == 1.50:
        dish = "espresso"
    elif amount == 2.50:
        dish == "latte"
    elif amount == 3.00:
        dish == "cappuccino"
    resources["water"]=resources["water"]-MENU[dish]["ingredients"]['water']
    resources["milk"]=resources["milk"]-MENU[dish]["ingredients"]['milk']
    resources["coffee"]=resources["coffee"]-MENU[dish]["ingredients"]['coffee']
    print(resources["water"])
    print(resources["milk"])
    print(resources["coffee"])
    print(f"Here is Your {dish}")
    

status = 'ON'
while status == 'ON':
    order=input("What would you like? (espresso/latte/cappuccino):")
    if order == "espresso":
        make(1.50)
    elif order == "latte":
        make(2.50)
    elif order == "cappuccino":
        make(3)
    elif order == "of":
        status = 'OF'
    elif order == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        Money = resources["dollar"]
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: {Money}")
    else:
        print("Enter Correct Input")
        



