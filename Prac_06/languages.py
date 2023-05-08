"""
Prac 06 CP1404 - Anastasia
"""
from Prac_06.ProgrammingLanguage import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
objects = [python, ruby, visual_basic]
[print(object) for thing in objects]
print("\nThe dynamically typed languages are:")
[print(thing.name) for thing in objects if thing.is_dynamic() if True]

"""The dynamically typed languages are:
Python
Ruby"""
