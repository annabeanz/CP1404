"""
Password checker

"""

key = input("Choose your password: ")
while len(key) < 10:
    print("Please input a password at least 10 characters in length")
    key = input("Choose your password: ")
for i in range(len(key)):
    print("*", end="")