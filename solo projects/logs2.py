import json

def create_message():
    num_lines = int(input("How many lines is your message? "))
    message = ""
    for i in range(num_lines):
        message += input() + "\n"
    key = input("Enter a key for your message: ")
    return key, message

messages_file = "messages.json"
messages = {}

# Load messages from file
try:
    with open(messages_file, "r") as f:
        messages = json.load(f)
except FileNotFoundError:
    pass

while True:
    print("\nMenu:")
    print("1. Create a new message")
    print("2. View a specific message")
    print("3. View all message keys")
    print("4. Delete a message")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key, message = create_message()
        messages[key] = message
        print("Message added successfully.")

    elif choice == "2":
        key = input("Enter the key of the message you want to view: ")
        if key in messages:
            print(messages[key])
        else:
            print("Message not found.")

    elif choice == "3":
        if messages:
            print("Message keys:")
            for key in messages:
                print(key)
            print("\n")
            while True:
                key_choice = input("Enter the key of the message you want to view or type 'exit': ")
                if key_choice == "exit":
                    break
                elif key_choice not in messages:
                    print("Invalid key. Please try again.")
                else:
                    print(messages[key_choice])
                    break
        else:
            print("No messages found.")

    elif choice == "4":
        key = input("Enter the key of the message you want to delete: ")
        if key in messages:
            del messages[key]
            print("Message deleted successfully.")
        else:
            print("Message not found.")

    elif choice == "5":
        # Save messages to file before exiting
        with open(messages_file, "w") as f:
            json.dump(messages, f)
        break

    else:
        print("Invalid choice. Please try again.")
