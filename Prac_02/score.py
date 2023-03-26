"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = get_score()
    score_rating(score)
    rand_score = get_random_score()
    print(rand_score)
    score_rating(rand_score)

def get_random_score():
    random_score = random.randint(0, 100)
    return random_score

def score_rating(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score

main()