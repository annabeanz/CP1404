"""
CP1404 - Practice & Extension Work
GPS (Gopher Population Simulator)
"""
import random

STARTING_POPULATION = 1000
INTRO = "Welcome to the Gopher Population Simulator!"
NUMBER_OF_YEARS = 10
DEATH_PERCENTAGE_LOWEST = 5
DEATH_PERCENTAGE_HIGHEST = 25
BIRTH_PERCENTAGE_LOWEST = 10
BIRTH_PERCENTAGE_HIGHEST = 20


def main():
    """Simulates gopher population fluctuation according to birth rate, death rate and number of years"""
    population = STARTING_POPULATION
    print(f"Starting population: {STARTING_POPULATION}")
    for year in range(NUMBER_OF_YEARS):
        print()
        print(f"Year {year + 1}")
        born = get_gophers_born(population)
        dead = get_gophers_dead(population)
        population = population + born - dead
        print(f"{born} gophers were born. {dead} died.")
        print(f"Population: {population}")
        year += 1


def get_gophers_dead(population):
    """Randomly assigns how many gophers from the total population are dead"""
    death_percentage = random.randint(DEATH_PERCENTAGE_LOWEST, DEATH_PERCENTAGE_HIGHEST)
    dead_gophers = (death_percentage / 100) * population
    return int(dead_gophers)


def get_gophers_born(population):
    """Randomly assigns how many gophers from the total population are born"""
    birth_percentage = random.randint(BIRTH_PERCENTAGE_LOWEST, BIRTH_PERCENTAGE_HIGHEST)
    new_gophers = (birth_percentage / 100) * population
    return int(new_gophers)

main()