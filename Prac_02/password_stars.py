"""
Password checker

"""
def main():
    key = get_password()
    out_stars(key)


def out_stars(key):
    for i in range(len(key)):
        print("*", end="")


def get_password():
    key = input("Choose your password: ")
    while len(key) < 10:
        print("Please input a password at least 10 characters in length")
        key = input("Choose your password: ")
    return key


main()