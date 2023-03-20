"""
CP1404 - Practical
Pseudocode for printing a star tree

get stars
for i in range(stars)
    for i in range(lines)
        print *


a and b and d of the question is missing
"""

stars = int(input("Number of stars: "))
for each_line in range(stars):
    for each_star in range(each_line +1):
        print("*", end='')
    print()


