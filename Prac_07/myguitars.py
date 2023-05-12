FILE_NAME = "guitars.csv"

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, previous):
        sorting_by_year = self.year < previous.year
        return sorting_by_year


def in_file(FILE_NAME):
    guitars = []
    with open(FILE_NAME, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',') # three variables have this position so no need to use index
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def out_file(FILE_NAME, guitars):
    with open(FILE_NAME, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    guitars = in_file(FILE_NAME)
    print("Existing Guitars:")
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost)
    print()
    while True:
        name = input("Enter guitar name - 'Q' to quit: ")
        if name.upper() == 'Q':
            break
        try:
            year = int(input("Enter guitar year: "))
            cost = int(input("Enter guitar cost: "))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
        except ValueError:
            print("A number has to be entered")
    out_file(FILE_NAME, guitars)
    print("Guitars saved to guitars.csv")


main()
