"""
Emails - name extractor using an email
"""


def main():
    """A program that records the users name and email"""
    email = input("Email:")
    names_emails = {}
    while email != "":
        if not ("@" in email):
            print("Invalid email")
        else:
            get_names_emails(email, names_emails)
        email = input("Email:")
    for name, email in names_emails.items():
        print(f"{name} ({email})", sep=" ")


def get_names_emails(email, names_emails):
    """Confirms the name information with the user, recording the correct name and email"""
    name = get_name(email)
    y_n = input(f"Is your name {name}? Y/N: ")
    if y_n.lower() != "y":
        name = input("Name: ")
    names_emails[name] = email
    return names_emails


def get_name(email):
    """extracts the name part from the email"""
    parts = email.split("@")
    name = parts[0]
    return name


main()
