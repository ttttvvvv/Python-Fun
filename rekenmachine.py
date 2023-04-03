#rekenmachine

print("+ voor plus \n - voor min \n * voor vermenigvuldigen \n / voor delen door")
andwoord = input("Wil je doorgaan J voor ja N voor nee \n")
while andwoord == "J":
    getal1 =float(input("Voer je eerste getal in : \n"))
    manier = input("Welke bewerking wil je doen : \n")
    getal2 = float(input("Voer je tweede getal in : \n"))

    if manier == "+":
        print(getal1 + getal2)
    if manier == "*":
        print(getal1 * getal2)
    elif manier == "-":
        print(getal1 - getal2)
    elif manier == "/":
        print(getal1 / getal2)
    andwoord = input("Wil je doorgaan J voor ja N voor nee \n")


else :
    quit()

