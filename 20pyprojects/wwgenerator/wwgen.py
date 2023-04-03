#Vraag of ze een ww willen genereren
#Vraag om lengte
#genereer ww
#print ww
#als ze op vraag 1 nee zeggen quit

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def genereer_ww():
    dienst = input("Voor welke platform of dienst gaat het gebruikt worden?\n--> ")
    gebruikersnaam = input("Welke gebruikersnaam heb je gebruikt?\n--> ")
    password_lengte = int(input("Hoe lang moet het wachtwoord zijn?\n--> "))

    random.shuffle(characters)

    wachtwoord = []

    for x in range(password_lengte):
        wachtwoord.append(random.choice(characters))

    random.shuffle(wachtwoord)

    wachtwoord = "".join(wachtwoord)

    print(wachtwoord)

    ww_database = open("ww_database.txt", "a")
    ww_database.write(f"\nPlatform: \n{dienst} \nGebruikersnaam : \n{gebruikersnaam} \nWachtwoord:\n{wachtwoord} \n")
    ww_database.close()


while True:
    option = input("Wil je een wachtwoord genereren (Ja/Nee)\n--> ")

    if option == "Ja" or option == "J" or option == "j" or option == "ja":
        genereer_ww()
    elif option == "Nee" or  option == "N" or option == "nee" or option == "n":
        print(" -------------Programma Beëndigd------------- ")
        quit()
    else:
        print("Fout ingevoerd")
    




