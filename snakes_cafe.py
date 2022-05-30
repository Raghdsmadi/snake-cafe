menu = """
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(menu)
def input_user():
    items = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Toranado", "A Litte Garden", "Ice Cream",
             "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
    quantities = {item: 0 for item in items}

    while True:
        value = input("> ")
        if value in items:
            quantities[value] += 1
            print(f"\n**{quantities[value]}order of {value} have been added to your meal**\n")
        elif value == "quit":
            break
        elif value == "meal":
            for i in [f"{key}: {val}" for key, val in quantities.items() if val != 0]:
                print(i)
        else:
            print(f"Sorry ... \"{value}\"is not on the menu.")

            while True:
                answer = input("Would you like to order anything else ? (y/n) : ")
                if (answer == "y") or (answer == "n"):
                    break
                else:

                    print("Please select \"y\" or \"n\"\n")

            if answer == "n":
                break


input_user()