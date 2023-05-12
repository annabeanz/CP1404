"""
Prac 06 CP1404 - Anastasia
"""
from ProgrammingLanguage import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991,"No")
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995,"No")
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991,"No")
languages = [python, ruby, visual_basic]
[print(thing) for thing in languages]
print("\nThe dynamically typed languages are:")
[print(thing.name) for thing in languages if thing.is_dynamic() if True]

"""The dynamically typed languages are:
Python
Ruby"""
