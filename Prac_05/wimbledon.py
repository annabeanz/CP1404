"""
Wimbledon file reader
"""

FILE_NAME = "wimbledon.csv"


def main():
    """A program that takes in a file of Wimbledon stats and displays the results"""
    year_to_info = process_in_file(FILE_NAME)
    champion_wins = get_champion_wins(year_to_info)
    countries = get_countries(year_to_info)
    for name, wins in champion_wins.items():
        print(f"{name} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(",".join(countries))


def get_countries(data):
    """Returns only the winning countries as a set"""
    countries = []
    for year, info in data.items():
        country = info[0]
        countries.append(country)
    return set(countries)


def get_champion_wins(data):
    """Tracks the number of wins for each champion"""
    champions = []
    for year, info in data.items():
        champion = info[1]
        champions.append(champion)
    champions.sort()
    win_diagnostics = champion_count(champions)
    return win_diagnostics


def champion_count(champion_list):
    """Counts occurrences of all the champions"""
    champion_wins = {}
    for champion in champion_list:
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins


def process_in_file(file):
    """Processes the in file of Wimbledon wins info and stores it as a dictionary"""
    year_to_info = {}
    with open(file, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = str(line)
            line_parts = line.split(",")
            year_to_info[line_parts[0]] = line_parts[1:]
    in_file.close()
    del year_to_info["Year"]
    return year_to_info


main()
