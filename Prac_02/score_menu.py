"""
CP1404/CP5632 - Practical
Score status using a menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = -1
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print("Your score has been recorded")
        elif choice == "P":
            if score > 0:
                rating = score_rating(score)
                print(score, rating)
            else:
                print("You need to first input a score to rate")
        elif choice == "S":
            if score > 0:
                for each in range(int(score)):
                    print("*", end="")
                print()
            else:
                print("You need to first input a score to print corresponding stars")
        else:
            print("Invalid input")
        choice = get_choice()
    print("Farewell")


def get_choice():
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def score_rating(score):
    if score >= 90:
        return "is Excellent"
    elif score >= 50:
        return "is Passable"
    elif score < 50:
        return "is Bad"


def get_valid_score():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
