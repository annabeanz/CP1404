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
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} °F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} °C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
