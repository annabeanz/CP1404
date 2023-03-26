"""
CP1404 - Practice & Extension Work
Temperature conversion using text files
"""

import random

NUMBER_OF_TEMPERATURES = 20
LOWEST_TEMP = -200
HIGHEST_TEMP = 200
NEW_FILE = "temps_input"
OUT_FILE = "temps_output"
MODE = "f to c"
# mode can be changed to "c to f" to convert celsius to fahrenheit


def main():
    """Program that takes in temperatures in a text file and converts it based on the MODE in a new out_file"""
    in_temp = []
    out_temp = []
    if_existing_file = get_which_file()
    if if_existing_file == "YES":
        in_file_name = choose_in_file()
    elif if_existing_file == "NO":
        generate_temps(in_temp)
        process_out_file(NEW_FILE, in_temp)
        in_file_name = NEW_FILE
    temps = process_in_file(in_file_name)
    convert_temperatures(out_temp, temps)
    process_out_file(OUT_FILE, out_temp)


def choose_in_file():
    """records the name of the custom in file"""
    choose_file = str(input("Please input the name of the existing file: "))
    while len(choose_file) <= 0:
        print("Please enter a valid file name")
        choose_file = str(input("Please input the name of the existing file: "))
    return choose_file


def get_which_file():
    """asks the user if they would like to use their own file, repeats until they answer yes or no"""
    ans = input(f"Would you like to use an existing file? ").upper()
    while ans != "YES" and ans != "NO":
        print("please answer yes or no")
        ans = input(f"Would you like to use an existing file? ").upper()
    return ans


def convert_temperatures(out_temp, temps):
    """designates which mode of conversion to use, this is according to the global value of MODE"""
    if MODE == "f to c":
        print("Converted temperatures from f to c")
        for temp in temps:
            temp = f_to_c(temp)
            out_temp.append(temp)
    elif MODE == "c to f":
        print("Converted temperatures from c to f")
        for temp in temps:
            temp = c_to_f(temp)
            out_temp.append(temp)


def process_in_file(file_name):
    """reads the text file and stores each line as a list"""
    temps = []
    in_file = open(file_name, "r")
    for line in in_file:
        temp = float(line)
        temps.append(temp)
    in_file.close()
    return temps


def generate_temps(in_temp):
    """generates a number of random temperatures and stores in a list"""
    for each in range(NUMBER_OF_TEMPERATURES):
        temp = round(random.uniform(LOWEST_TEMP, HIGHEST_TEMP), 2)
        in_temp.append(temp)


def process_out_file(file_name, lines):
    """Prints the converted temperatures in a list to a designated out_file line by line"""
    out_file = open(file_name, "w")
    for line in lines:
        print(f"{line:,.2f}", file=out_file)
    out_file.close()


def f_to_c(fahrenheit):
    """converts a fahrenheit value to celsius"""
    result = 5 / 9 * (fahrenheit - 32)
    return result


def c_to_f(celsius):
    """converts a celsius value to fahrenheit"""
    result = celsius * 9.0 / 5 + 32
    return result


main()
