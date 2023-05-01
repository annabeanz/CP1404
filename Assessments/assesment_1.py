"""
CP1404 - Assessment: Travel tracker
Anastasia Eremenko
Menu driven travel tracker
"""
import random

MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - " \
       "Quit\n>>> """
VALID_MENU_INPUT = ("1", "L", "2", "R", "3", "A", "4", "M" "5", "Q")

IN_FILE = "places.csv"


def main():
    """Menu-driven travel tracker"""
    places = process_in_file(IN_FILE)
    choice = load_choice(MENU)
    execute_menu(choice, places)
    while choice != "Q":
        choice = load_choice(MENU)
        execute_menu(choice, places)
    process_outfile(places)
    print("Goodbye")


def load_choice(thing):
    """Ensures that only a valid choice can be entered"""
    validated = False
    choice = str(input(thing)).upper()
    while not validated:
        for valid_input in VALID_MENU_INPUT:
            if choice == valid_input:
                validated = True
                break
        if not validated:
            print("Invalid menu choice")
            choice = str(input(thing)).upper()
    return choice


def process_in_file(file):
    """Processes the in file of places and stores it as a list"""
    city_to_visit_stats = {}
    with open(file, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = str(line)
            line_parts = line.split(",")
            city_to_visit_stats[line_parts[0]] = line_parts[1:]
    in_file.close()
    return city_to_visit_stats


def execute_menu(choice, places):
    """Executes the user's selected menu option"""
    if choice == VALID_MENU_INPUT[0] or choice == VALID_MENU_INPUT[1]:
        list_places(places)
    if choice == VALID_MENU_INPUT[2] or choice == VALID_MENU_INPUT[3]:
        print("Not sure where to visit next?")
        city, location_details = get_unvisited_place(places)
        print(f"How about {city} in {location_details[0]}?")
    if choice == VALID_MENU_INPUT[4] or choice == VALID_MENU_INPUT[5]:
        name = not_blank("Name: ", "str")
        country = not_blank("Country: ", "str")
        priority = not_blank("Priority: ", "int")
        places[name] = [country, priority, "n"]
        print(f"{name} in {country} of priority {priority} added to Travel Tracker")
    if choice == VALID_MENU_INPUT[6] or choice == VALID_MENU_INPUT[7]:
        all_numbers, unvisited_numbers = get_list_values(places)
        list_places(places)
        total_places, unvisited_count = get_unvisited_places(places, 1)
        number_obtained = get_valid_visited_number(places, total_places, unvisited_count)
        if_already_visited(all_numbers, number_obtained, places, unvisited_numbers)


def if_already_visited(all_numbers, number_obtained, places, unvisited_numbers):
    """Checks whether the chosen place has already been marked as visited."""
    if number_obtained not in all_numbers:
        print("The number has to be from the list! - Returning to menu.")
    if number_obtained in all_numbers and number_obtained not in unvisited_numbers:
        for city, info in places.items():
            if number_obtained == int(info[1]):
                print(f"{city} in {info[0]} already visited!")


def get_list_values(places):
    """Returns only the priority values as a list from dictionaries"""
    unvisited_numbers = []
    unvisited = get_unvisited_places(places, 2)
    unvisited_info = list(unvisited.values())
    for parameter in unvisited_info:
        unvisited_numbers.append(int(parameter[1]))
    all_numbers = []
    all_info = list(places.values())
    for parameter in all_info:
        all_numbers.append(int(parameter[1]))
    return all_numbers, unvisited_numbers


def not_blank(prompt, verification_type):
    """Ensures that the user input is not blank."""
    name = input(prompt)
    while len(name) == 0:
        print("Input cannot be blank")
        name = input(prompt)
    if verification_type == "int":
        while not name.isdigit():
            print("Input has to be a number")
            name = input(prompt)
    return name


def get_unvisited_place(places):
    """Returns the details of a random unvisited place."""
    unvisited_places = get_unvisited_places(places, 2)
    index_to_visit = random.randint(1, len(unvisited_places))
    city = list(unvisited_places.keys())[index_to_visit - 1]
    location_details = unvisited_places[city]
    return city, location_details


def get_valid_visited_number(places, total_places, unvisited_count):
    """Prompts the user to select their visited number from the list of priorities"""
    number_obtained = False
    while not number_obtained:
        try:
            visit_change_num = int(
                input(f"Out of {total_places} places, you want to visit {unvisited_count}\nEnter the "
                      f"number of the place you want to mark as visited\n>>>"))
            unvisited_country_to_nums = {}
            for country, info in places.items():
                if info[2].strip() == "n":
                    unvisited_country_to_nums[country] = list(info)[1]
                if info[2].strip() == "v":
                    number_obtained = True
                    break
            for country, number in unvisited_country_to_nums.items():
                if visit_change_num == int(number):
                    places[country][2] = "v"
                    number_obtained = True
                    break
        except ValueError:
            print("It must be a number")
    return visit_change_num


def get_unvisited_places(places, mode):
    """Returns the unvisited places count in mode 1, returns a dictionary of unvisited places in mode 2"""
    unvisited = {}
    unvisited_count = 0
    for key in list(places.keys()):
        total_places = len(places)
        item = places[key]
        if item[-1].strip() != "v":
            unvisited_count += 1
            unvisited[key] = item
    if mode == 1:
        return total_places, unvisited_count
    if mode == 2:
        return unvisited


def list_places(places):
    """Displays formatted, sorted list of places and their visit status"""
    longest_city, longest_country = get_longest_info(places)
    index = 1
    keys = list(places.keys())
    keys.sort()
    types_to_sort = ["*", " "]
    for sorting_type in types_to_sort:
        for location in keys:
            visit_status = visits(places[location])
            if visit_status == sorting_type:
                print(f"{visit_status}{index}. {location:<{longest_city}} in {places[location][0]:<{longest_country}} "
                      f"{places[location][1]:>3}")
                index += 1


def visits(place):
    """Returns the * indicator for visited places"""
    if place[-1].strip() != "v":
        return "*"
    else:
        return " "


def get_longest_info(places):
    """Returns the number of spaces needed to format the place names in columns"""
    countries = []
    for city, info in places.items():
        countries.append(info[0])
    longest_country = get_longest_word(countries)
    longest_city = get_longest_word(places.keys())
    return longest_city, longest_country


def get_longest_word(words):
    """Gets the length of the longest place and returns it as an integer"""
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word

def process_outfile(places):
    with open(IN_FILE, "w") as in_file:
        for key, value in places.items():
            in_file.write(f"{key},{value[0]},{value[1]}\n")

main()
