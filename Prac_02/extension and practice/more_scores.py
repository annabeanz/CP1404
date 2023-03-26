"""
CP1404 - Practice & Extension Work
more scores exercise
"""

import random


def main():
    scores = []
    results = []
    number_of_scores = get_number_of_scores()
    generate_random_scores(number_of_scores, scores)
    get_ratings(results, scores)
    process_out_file(results)
    print("The results are posted in a new or exiting txt file named (results)")


def get_ratings(results, scores):
    for score in scores:
        rating = score_rating(score)
        formatted_rating = f"{score} is {rating}"
        results.append(formatted_rating)
    return results


def generate_random_scores(number_of_scores, scores):
    for score in range(number_of_scores):
        score = random.randint(0, 100)
        scores.append(score)
    return scores


def get_number_of_scores():
    number_of_scores = int(input("How many scores: "))
    while number_of_scores > 100 or number_of_scores <= 0:
        print("Please enter a valid number of scores")
        number_of_scores = int(input("How many scores: "))
    return number_of_scores


def score_rating(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


def process_out_file(lines):
    """Reads the lines stored in a list and prints them to a new out file (results)"""
    out_file = open("results", "w")
    for line in lines:
        print(line, file=out_file)
    out_file.close()


main()
