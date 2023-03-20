"""
CP1404 - Practical
Pseudocode for a menu-driven hello/goodbye interaction

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
INVALID_MESSAGE = "Invalid Input"
FINISHED_MESSAGE = "Finished."

name = input("Enter Name: ")
print(MENU)
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print(INVALID_MESSAGE)
    print(MENU)
    choice = input("Choice: ").upper()
print(FINISHED_MESSAGE)
