"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
def main():
    try:
        numerator = above_zero("Enter the numerator: ")
        denominator = above_zero("Enter the denominator: ")
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

def above_zero(prompt):
    number = int(input(prompt))
    while number == 0:
        print("this cannot be a 0")
        number = int(input(prompt))
    return number



main()
"""
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# 1. When either the numerator or denominator are not integer-numbers or are anything other than numeric
# 2. When the denominator is 0, this results in an infinite number that python does not recognise
# 3. Include an error checking loop so the number inputted will be above 0
