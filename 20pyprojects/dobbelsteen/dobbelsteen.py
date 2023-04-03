# import random
# definieër de functie om de dobbelsteen te rollen
# maak een dictionary voor de tekeningen van de dobbelsteen

import random

def roll_dice():
    steen_tekening = {
    1: (
        "┌─────────┐",
        "│    1    │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│    2    │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ● 3    │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    4    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ● 5 ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ● 6 ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    }

    roll = input("Rol de dobbelsteen (Ja/Nee):\n-->")

    while roll.lower() == "Ja".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dobbelsteen gerold {} en {}".format(dice1, dice2))
        print("\n".join(steen_tekening[dice1]))
        print("\n".join(steen_tekening[dice2]))
        roll = input("Rol opnieuw? (Ja/Nee)\n-->")

roll_dice()
