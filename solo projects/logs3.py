import os.path
import json

messages = {}

def save_messages():
    with open('messages.json', 'w') as file:
        json.dump(messages, file)

def load_messages():
    global messages
    if os.path.exists('messages.json'):
        with open('messages.json', 'r') as file:
            messages = json.load(file)

def add_message():
    key = input("Enter a key for the message: ")
    num_lines = int(input("How many lines is your message? "))
    message = ""
    for i in range(num_lines):
        line = input(f"Enter line {i+1}: ")
        message += line + "\n"
    messages[key] = message

def view_all_messages():
    if not messages:
        print("No messages found.")
    else:
        for key in messages.keys():
            print(key)

def view_message():
    if not messages:
        print("No messages found.")
    else:
        key = input("Enter the key of the message you want to view: ")
        while key not in messages.keys():
            if key.lower() == "exit":
                return
            print("Invalid key. Try again or type 'exit' to cancel.")
            key = input("Enter the key of the message you want to view: ")
        print(messages[key])

def delete_message():
    if not messages:
        print("No messages found.")
    else:
        key = input("Enter the key of the message you want to delete: ")
        while key not in messages.keys():
            if key.lower() == "exit":
                return
            print("Invalid key. Try again or type 'exit' to cancel.")
            key = input("Enter the key of the message you want to delete: ")
        del messages[key]
        print("Message deleted.")

def main():
    load_messages()
    while True:
        print("Message Storage Program\n")
        print("1. Add a message")
        print("2. View all messages")
        print("3. View a specific message")
        print("4. Delete a message")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_message()
        elif choice == "2":
            view_all_messages()
        elif choice == "3":
            view_message()
        elif choice == "4":
            delete_message()
        elif choice == "5":
            save_messages()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == '__main__':
    main()
