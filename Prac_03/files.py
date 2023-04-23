"""
CP1404/CP5632 - Practical
Asks the user for their name, then opens a file called "name.txt" and writes that name to it
Code that opens "name.txt" and reads the name (as above) then prints the formatted name into the file
Code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result
Code that prints the total for all lines in numbers.txt or a file with any number of numbers
"""


def question_01():
    name = input("Name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()


def question_02():
    in_file_line = open("name.txt", "r")
    name = in_file_line
    formatted_name = f"Your name is {name}."
    out_file = open("name.txt", "w")
    print(formatted_name, file=out_file)
    out_file.close()


def question_03():
    in_file_lines = open("numbers", "r")
    number_1 = in_file_lines[0]
    number_2 = in_file_lines[1]
    total = number_1 + number_2
    print(total)
question_03()


def question_04():
    """reads the text file and stores each line as a list"""
    in_file = open("numbers.txt", "r")
    for line in in_file:
        print(line)
    in_file.close()
















