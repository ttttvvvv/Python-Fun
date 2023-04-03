#definieer de functies die je nodig hebt 

getal1 = int(input("Voer je eerste getal in: "))
getal2 = int(input("Voer je tweede getal in: "))
methode = input("Welke methode wilt je gebruiken: ")
andwoord = ''




def rekenmachine():
    
        if methode == "/":
            andwoord = getal1 / getal2
        elif methode == "+":
            andwoord = getal1 + getal2 
        elif methode == "-":
            andwoord = getal1 - getal2
        else:
            andwoord = getal1 * getal2

        print(f"Jou andwoord is: {andwoord}")
  


rekenmachine()

quit()




