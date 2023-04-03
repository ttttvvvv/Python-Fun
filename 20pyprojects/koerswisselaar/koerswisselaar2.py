#creer functies die later met elkaar gelinkt worden 
#a is euro

#moet nog aan gewerkt worden puntjes op de i

# aanpassen maak een api die de data opvraagt met hulp van een functie 

while True:
    
    print("")
    print("")
    print("Maak uw keuze:")
    print("A: Dollar (USD)")
    print("B: Euro (EUR)")
    print("C: Pond (GPB)")
    print("D: Zwitserse Frank (CHF)")
    print("E: Canadese Dollar (CAD)")
    print("F: Yen (CNY)")
    print("Q: Quit")
    keuze1 = input("Keuze 1-->  ")
    keuze2 = input("Keuze 2-->  ")

    # Keuze A

    if keuze1 == "a":
        aantal = float(input("Hoeveel Dollar wil je wisselen: "))
    if keuze2 == "b" and keuze1 == "a":
        gewisseld_bedrag = aantal * float(0.92)
    elif keuze2 == "c" and keuze1 == "a":
        gewisseld_bedrag = aantal * float(0.81)
    elif keuze2 == "d" and keuze1 == "a":
        gewisseld_bedrag = aantal * float(0.92)
    elif keuze2 == "e" and keuze1 == "a":
        gewisseld_bedrag = aantal * float(1.35)
    elif keuze2 == "f" and keuze1 == "a":
        gewisseld_bedrag = aantal * float(6.87)


    # Keuze B

    if keuze1 == "b":
        aantal = float(input("Hoeveel Euro wil je wisselen: "))
    if keuze2 == "a" and keuze1 == "b":
        gewisseld_bedrag = aantal * float(0.92)
    elif keuze2 == "c" and keuze1 == "b":
        gewisseld_bedrag = aantal * float(0.88)
    elif keuze2 == "d" and keuze1 == "b":
        gewisseld_bedrag = aantal * float(0.92)
    elif keuze2 == "e" and keuze1 == "b":
        gewisseld_bedrag = aantal * float(0.99)
    elif keuze2 == "f" and keuze1 == "b":
        gewisseld_bedrag = aantal * float(7.45)


    # Keuze C

    if keuze1 == "c":
        aantal = float(input("Hoeveel Pond wil je wisselen: "))
    if keuze2 == "a" and keuze1 == "c":
        gewisseld_bedrag = aantal * float(1.23)
    elif keuze2 == "b" and keuze1 == "c":
        gewisseld_bedrag = aantal * float(1.14)
    elif keuze2 == "d" and keuze1 == "c":
        gewisseld_bedrag = aantal * float(1.13)
    elif keuze2 == "e" and keuze1 == "c":
        gewisseld_bedrag = aantal * float(1.67)
    elif keuze2 == "f" and keuze1 == "c":
        gewisseld_bedrag = aantal * float(8.47)

    # Keuze D

    if keuze1 == "d":
        aantal = float(input("Hoeveel Zwitserse Frank wil je wisselen: "))
    if keuze2 == "a" and keuze1 == "d":
        gewisseld_bedrag = aantal * float(1.09)
    elif keuze2 == "b" and keuze1 == "d":
        gewisseld_bedrag = aantal * float(1.01)
    elif keuze2 == "c" and keuze1 == "d":
        gewisseld_bedrag = aantal * float(0.89)
    elif keuze2 == "e" and keuze1 == "d":
        gewisseld_bedrag = aantal * float(1.48)
    elif keuze2 == "f" and keuze1 == "d":
        gewisseld_bedrag = aantal * float(7.50)

    # Keuze E

    if keuze1 == "e":
        aantal = float(input("Hoeveel Canadese Dollar wil je wisselen: "))
    if keuze2 == "a" and keuze1 == "e":
        gewisseld_bedrag = aantal * float(0.74)
    elif keuze2 == "b" and keuze1 == "e":
        gewisseld_bedrag = aantal * float(0.68)
    elif keuze2 == "c" and keuze1 == "e":
        gewisseld_bedrag = aantal * float(0.60)
    elif keuze2 == "d" and keuze1 == "e":
        gewisseld_bedrag = aantal * float(0.68)
    elif keuze2 == "f" and keuze1 == "e":
        gewisseld_bedrag = aantal * float(5.08)


    # Keuze F

    if keuze1 == "f":
        aantal = float(input("Hoeveel Yen wil je wisselen: "))
    if keuze2 == "a" and keuze1 == "f":
        gewisseld_bedrag = aantal * float(0.15)
    elif keuze2 == "b" and keuze1 == "f":
        gewisseld_bedrag = aantal * float(0.13)
    elif keuze2 == "c" and keuze1 == "f":
        gewisseld_bedrag = aantal * float(0.12)
    elif keuze2 == "d" and keuze1 == "f":
        gewisseld_bedrag = aantal * float(0.13)
    elif keuze2 == "e" and keuze1 == "f":
        gewisseld_bedrag = aantal * float(0.20)

    if keuze1 == "q" and keuze2 == "q" or keuze1 == "q" and keuze2 == "":
        quit()

    
    print("")
    print("")
    print("Te ontvangen bedrag: ", float(gewisseld_bedrag))


