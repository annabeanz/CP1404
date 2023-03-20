"""
CP1404 - Practical
Pseudocode for sales bonus calculation

function main()
    get sales
    while sales > 0
        determine_bonus(sales)
        display bonus
        get sales

function determine_bonus(sales)
    if sales < 1000
        bonus = sales * 0.1
    else if sales >= 1000
        bonus = sales * 0.15
    return bonus
"""


def sales_bonus():
    """A program which determines and displays the user sales bonus"""
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = determine_bonus(sales)
        print(f"Your bonus is: {bonus:,.2f}")
        sales = float(input("Enter sales: $"))


def determine_bonus(sales):
    """Determines the bonus amount based on sales amount"""
    if sales < 1000:
        bonus = sales * 0.1
    elif sales >= 1000:
        bonus = sales * 0.15
    return bonus


sales_bonus()
