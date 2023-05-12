"""
Prac 06 CP1404 - Anastasia

Expected Time: 1 hour
Actual Time: 19 min
"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="N/A",reflection= "N/A",year = 0, pointer = "N/A"):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name
        self.pointer = pointer

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def is_pointer(self):
        if self.pointer == "Yes":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}," \
               f"Pointer Arithmetic={self.pointer}"
