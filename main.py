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
def resource_change(ingredients,resource_amount):
    '''get ingredient and resources, return formatted resource if there is enough resources else return print'''
    new_resources = {}
    if "milk" in ingredients:
        new_resources["milk"] = resource_amount["milk"] - ingredients["milk"]
    else:
        new_resources["milk"] = resource_amount["milk"]

    new_resources["water"] = resource_amount["water"] - ingredients["water"]
    new_resources["coffee"] = resource_amount["coffee"] - ingredients["coffee"]

    if new_resources["water"] < 0:
        return "Sorry there is not enough water."

    elif new_resources["milk"] < 0:
        return "Sorry there is not enough milk."

    elif new_resources["coffee"] < 0:
        return "Sorry there is not enough coffee."
    else:
        return new_resources

def report(money):
    """print resources amount and money"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def user_choice_control(choice):
    """get user_choice and return menu choice or report"""
    if choice == "espresso":
        return MENU["espresso"]
    elif choice == "latte":
        return MENU["latte"]
    elif choice == "cappuccino":
        return MENU["cappuccino"]
    elif choice == "report":
        return "report"
    elif choice == "off": #off line yapar uygulamadan çıkartır
        return False

def money_count(cost):
    """input product cost and get user's money and return change or answer """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    count = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    count = round(count,2)
    return count

def coffeeMachine():
    global resources
    is_machine_on = True
    money = 0
    while is_machine_on:
        user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
        user_choice_name = user_choice
        user_choice = user_choice_control(user_choice)
        if user_choice == False:
            is_machine_on = False
        elif user_choice == "report":
            report(money)
        else:
            resource_answer = resource_change(user_choice["ingredients"], resources)
            if type(resource_answer) == str:
                print(resource_answer)
            else:
                cost = user_choice["cost"]
                resources = resource_answer
                count = money_count(cost)
                if count < cost:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${count - cost} dollars in change.")
                    print(f"Here is your {user_choice_name}. Enjoy!")
                    money += cost

coffeeMachine()