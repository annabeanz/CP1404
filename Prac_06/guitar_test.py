"""
Prac 06 CP1404 - Anastasia

Gibson L-5 CES get_age() - Expected 100. Got 100
Another Guitar get_age() - Expected 9. Got 9
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
"""

from Prac_06.guitar import Guitar

# guitars
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)

# The expected values have been adjusted to fit year 2023
print(f"""Gibson L-5 CES get_age() - Expected 101. Got {gibson.get_age()}
Another Guitar get_age() - Expected 10. Got {another_guitar.get_age()}
Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}
Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}""")
