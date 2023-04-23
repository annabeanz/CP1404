colour_to_code = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_to_code[colour_name])
        colour_name = input("Enter colour name: ").lower()
    except KeyError:
        print("Invalid colour")
        colour_name = input("Enter colour name: ").lower()
