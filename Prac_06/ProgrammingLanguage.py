"""
Prac 06 CP1404 - Anastasia

Expected Time: 1 hour
Actual Time: 19 min
"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="N/A",reflection= "N/A",year = 0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
