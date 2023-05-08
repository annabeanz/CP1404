"""
Prac 06 CP1404 - Anastasia
"""

from Prac_06.guitar import Guitar


def main():
    """A program that prompts the user for their guitar info's and displays a summary"""
    print("My guitars!")
    guitars = []
    guitar_names = []
    costs = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        guitar_names.append(guitar.name)
        costs.append(cost)
        print("{} added.".format(guitar))
        name = input("Name: ")

    print("\nThese are my guitars:")
    longest_guitar_name = get_longest_word_length(guitar_names)
    largest_cost = get_longest_word_length(costs)
    for number, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_message = "(vintage)"
        else:
            vintage_message = ""
        print(
            f"Guitar {number}: {guitar.name:>{longest_guitar_name}} ({guitar.year}), worth "
            f"${guitar.cost:>{largest_cost},.2f}{vintage_message}")


def get_longest_word_length(words):
    """Returns the number of spaces needed to format the guitar parameters in columns"""
    longest_word = 0
    for word in words:
        word = str(word)
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word


main()
