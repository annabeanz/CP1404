"""Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Note the formatting below so that numbers align neatly.
"""
import random

LOWEST_NUMBER = 0
HIGHEST_NUMBER = 45
LOWEST_NUMBER_PICKS = 0
HIGHEST_NUMBER_PICKS = 100
NUMBERS_EACH_LINE = 6


def main():
    """Asks the user for the number of 6-digit lottery picks, generates and displays the picks"""
    no_of_picks = get_user_number("How many quick picks?: ")
    table = generate_picks(no_of_picks)
    for line in table:
        print()
        for number in line:
            print(f"{number:>2}", end=" ")


def generate_picks(no_of_picks):
    """Generates a table of picks as a nested list"""
    table = []
    for each_row in range(no_of_picks):
        line_of_numbers = []
        for number in range(NUMBERS_EACH_LINE):
            num = get_rand_number()
            while num in line_of_numbers:
                num = get_rand_number()
            line_of_numbers.append(num)
        table.append(line_of_numbers)
    return table


def get_user_number(prompt):
    """Ensures the input by the user is an integer number within set bounds"""
    invalid_number = True
    while invalid_number:
        try:
            number = int(input(prompt))
            while number < LOWEST_NUMBER_PICKS or number > HIGHEST_NUMBER_PICKS:
                print("The number is out of bounds")
                number = int(input(prompt))
            invalid_number = False
        except ValueError:
            print("That is not an integer number")
    return number


def get_rand_number():
    return random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)


main()
