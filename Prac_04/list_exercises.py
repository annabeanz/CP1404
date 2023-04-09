#  Basic list operations

QTT_NUMBERS = 5
LOWEST = 0
HIGHEST = 100


def number_chooser():
    """Collects a range of numbers from the user then displaying the first,last,smallest,largest and average number"""
    numbers = []
    for i in range(QTT_NUMBERS):
        number = get_valid_number(f"Number {i + 1}: ")
        numbers.append(number)
    first = f"The first number is: {numbers[0]}"
    last = f"The last number is: {numbers[-1]}"
    smallest = f"The smallest number is: {min(numbers)}"
    largest = f"The largest number is: {max(numbers)}"
    average = f"The average of all the numbers is: {(sum(numbers) / len(numbers)):.2f}"
    print(first, last, smallest, largest, average, sep="\n")


def get_valid_number(prompt):
    """Checks if the input is a number float, if not re-prompts the user for a number"""
    is_number = False
    while not is_number:
        try:
            number = float(input(prompt))
            is_number = True
        except ValueError:
            print("it has to be a number")
    while number < LOWEST or number > HIGHEST:
        print("Number not within the permitted range")
        number = int(input(prompt))
    return number


number_chooser()


#  Woefully inadequate security checker


VALID_USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', " \
                  "'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', " \
                  "'InterpreterInterface', 'StartServer', 'bob']


def usernames():
    """Takes a username input and only grants access to only a list of valid usernames"""
    grant_access = False
    user = str(input("Enter your username: "))
    for valid_username in VALID_USERNAMES:
        if valid_username == user:
            grant_access = True
    if grant_access:
        print("Access granted")
    else:
        print("Access denied")


usernames()
