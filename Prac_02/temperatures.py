"""
CP1404- Practical
Pseudocode for temperature conversion

print menu
get choice
while choice != Q
    if choice == C
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        print fahrenheit
    else if choice == F
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        print celsius
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = get_celcius()
            result = c_to_f(celsius)
            print(f"Result: {result:.2f} °F")
        elif choice == "F":
            fahrenheit = get_fahrenheit()
            result = f_to_c(fahrenheit)
            print(f"Result: {result:.2f} °C")
        else:
            print("Invalid option")
        choice = get_choice()
    print("Thank you.")


def f_to_c(fahrenheit):
    result = 5 / 9 * (fahrenheit - 32)
    return result


def get_fahrenheit():
    fahrenheit = float(input("fahrenheit: "))
    return fahrenheit


def c_to_f(celsius):
    result = celsius * 9.0 / 5 + 32
    return result



def get_celcius():
    celsius = float(input("Celsius: "))
    return celsius


def get_choice():
    print(MENU)
    choice = input(">>> ").upper()
    return choice

main()