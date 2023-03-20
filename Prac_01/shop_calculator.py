"""
CP1404 - Practical
Pseudocode for calculating a total for a set number of items

function main
    total = 0
    items_number = error_check_items_number("prompt")
    for i in range (items number)
        item_price = error_check_items_price("prompt")
        total += item_price
    print total, items_numer

function error_check_items_number
    get items_number
        if items_number <= 0
            print "Invalid"
            get items_number

function error_check_items_price
    get item_price
        if items_number <= 0
            print "Invalid"
            get item_price

forgot 10% discount
"""


def main():
    """Calculator of the total price based on the number of items and their costs"""
    items_number = error_check_items_number("Number of items: ")
    total = 0
    for item in range(items_number):
        item_price = error_check_items_price(f"Item {item + 1} price: ")
        total += item_price
    print(f"Total price for {items_number} items is ${total:,.2f}")


def error_check_items_number(prompt):
    """Checks that the item number is above 0, returns as an integer"""
    user_in = int(input(prompt))
    while user_in <= 0:
        print("Invalid Input")
        user_in = int(input(prompt))
    return user_in


def error_check_items_price(prompt):
    """Checks the item price to be above 0, returns a float"""
    user_in = float(input(prompt))
    while user_in <= 0:
        print("Invalid Input")
        user_in = float(input(prompt))
    return user_in


main()
