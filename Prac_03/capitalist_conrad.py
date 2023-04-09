import os.path

def create_message():
    message = []
    key = input("Enter key for the message: ")
    num_lines = int(input("Enter number of lines for the message: "))
    print("Enter message content:")
    for i in range(num_lines):
        line = input()
        message.append(line)
    messages[key] = message

def view_all_messages():
    if len(messages) == 0:
        print("No messages found.")
    else:
        print("Keys:")
        for key in messages:
            print(key)
        print()
        key = input("Enter key for message to view: ")
        if key in messages:
            message = messages[key]
            print("\n".join(message))
        else:
            print("Key not found.")

def delete_message():
    if len(messages) == 0:
        print("No messages found.")
    else:
        print("Keys:")
        for key in messages:
            print(key)
        print()
        key = input("Enter key for message to delete: ")
        if key in messages:
            del messages[key]
            print("Message deleted.")
        else:
            print("Key not found.")

def copy_paste_message():
    key = input("Enter key for the message: ")
    message = input("Enter message content: ")
    messages[key] = message.splitlines()

def save_messages_to_file():
    with open("messages.txt", "w") as file:
        for key, message in messages.items():
            file.write(key + "\n")
            for line in message:
                file.write(line + "\n")
            file.write("\n")

def load_messages_from_file():
    if not os.path.isfile("messages.txt"):
        return
    with open("messages.txt", "r") as file:
        lines = file.readlines()
        key = ""
        message = []
        for line in lines:
            if line.strip() == "":
                messages[key] = message
                key = ""
                message = []
            elif key == "":
                key = line.strip()
            else:
                message.append(line.strip())

messages = {}

load_messages_from_file()

while True:
    print("Menu:")
    print("1. Create message")
    print("2. View all messages")
    print("3. View specific message")
    print("4. Delete message")
    print("5. Copy and paste message")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_message()
    elif choice == "2":
        view_all_messages()
    elif choice == "3":
        view_all_messages()
    elif choice == "4":
        delete_message()
    elif choice == "5":
        copy_paste_message()
    elif choice == "6":
        save_messages_to_file()
        break
    else:
        print("Invalid choice. Please try again.")