"""
CP1404 - Extension
Pseudocode for a menu-driven sequence generation

function main()
    display menu
    input = verify_menu_choice(prompt)
    while input != 4
        if input == 1
            get start_number
            get end_number
            even_numbers = is_even(start, end)
            display even_numbers
        else if input == 2
            get start_number
            get end_number
            odd_numbers = is_odd(start, end)
            display odd_numbers
        else if input == 3
            get start_number
            get end_number
            square_numbers = is_square(start, end)
            display square_numbers

function verify_menu_choice(prompt)
    get input
    if input != 1 and input != 2 and input != 3 and input !=4
        print "Invalid input"
        get input

function is_even(start, end)
    numbers = []
    for number in range(start, end)
        if number % 2 == 0
        number append to numbers

function is_odd(start, end)
    numbers = []
    for number in range(start, end)
        if number % 2 == 1
        number append to numbers

function is_square(start, end)
    numbers = []
    for number in range(start, end)
        if (number / number) == number
        number append to numbers
"""

MENU = "1) Show the even numbers from x to y\n2) Show the odd numbers from x to y\n3) Show the squares from x to y 4)" \
       "\n4) Exit the program"


def main():
    print(MENU)
    choice = verify_menu_choice("Choose option (1-4): ")
    while choice != 4:
        if choice == 1:
            start_number = int(input("What is your starting number?: "))
            end_number = int(input("What is your ending number?: "))
            even_numbers = is_even(start_number, end_number)
            print(even_numbers)
        elif choice == 2:
            start_number = int(input("What is your starting number?: "))
            end_number = int(input("What is your ending number?: "))
            odd_numbers = is_odd(start_number, end_number)
            print(odd_numbers)
        elif choice == 3:
            start_number = int(input("What is your starting number?: "))
            end_number = int(input("What is your ending number?: "))
            square_numbers = is_square(start_number, end_number)
            print(square_numbers)
        print(MENU)
        choice = verify_menu_choice("Choose option (1-4): ")
    print("Goodbye.")


def verify_menu_choice(prompt):
    choice = int(input(prompt))
    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Invalid input")
        choice = int(input(prompt))
    return choice


def is_even(start, end):
    numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            numbers.append(number)
    return numbers


def is_odd(start, end):
    numbers = []
    for number in range(start, end + 1):
        if number % 2 == 1:
            numbers.append(number)
    return numbers


def is_square(start, end):
    numbers = []
    for number in range(start, end + 1):
        for i in range(end + 1):
            if int(i) ** 2 == number:
                numbers.append(number)
    return numbers


main()
