"""
Prac 06 CP1404 - Anastasia
"""


class Guitar:
    """Represents the guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.cost = cost
        self.year = year

    def is_vintage(self):
        """Returns a boolean if the guitar is vintage"""
        return self.get_age() >= 50

    def get_age(self):
        """Returns the age of the guitar based on year 2023"""
        return 2023 - self.year

    def __str__(self):
        """Formats the output"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
