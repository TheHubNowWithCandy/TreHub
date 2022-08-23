from time import sleep


LICENSES = ["MIT License",
            "GNU GPLv3",
            "GNU APGLv3",
            "Mozilla Public License 2.0",
            "Apache License 2.0",
            "Boost Software License 1.0",
            "The Unlicensed"
           ]

ASCII_ART = """\
___________                ___ ___      ___.      *
\__    ___/______   ____  /   |   \ __ _\_ |__    *
  |    |  \_  __ \_/ __ \/    ~    \  |  \ __ \\   *
  |    |   |  | \/\  ___/\    Y    /  |  / \_\ \\  *
  |____|   |__|    \___  >\___|_  /|____/|___  /  *
                       \/       \/           \/   *"""

print("*"*48, "\\")
print(ASCII_ART)
print("*"*48, "/", "\n")


# List a number of possible licenses
print("Let's find out which license fits best for your project\n")
print("There are many licenses to pick from:\n")
for license in LICENSES:
    print(f"\t-{license}")
print()


# Give the user the illusion of a choice
input("Do you just want to populate your Github account in order\n"
      "to show off your coding skills for a job application? [y/n]: ")
print()
# Waste some time before coming to the conclusion to use the MIT license
input("Just starting out, creating an easy application such as\n"
        "a simple calculator or minesweeper with a GUI? [y/n]: ")
print()
sleep(0.7)
print(f"You can't go wrong choosing the {LICENSES[0]}")
