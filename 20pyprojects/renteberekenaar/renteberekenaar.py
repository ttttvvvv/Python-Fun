# welke input heb je nodig: leen bedrag, jaarljkse rente, aantal jaren om terug te betalen
# bereken de maandelijkse betaling
# return dat aan de gebruiker

def main():
    print(" Dit is een maandelijkse rentetarief berekenaar ")
    print("")


    lening = float(input("Hoeveel heb je geleend : "))
    apr = float(input("Wat is de jaarlijkse rente percentage : "))
    jaren = float(input("Binnen hoeveel jaar ga je betalen : "))

    maandelijks_rente = apr / 1200
    aantal_maanden = jaren * 12 
    maandelijks_kosten = lening * maandelijks_rente / (1- (1 + maandelijks_rente) ** (-aantal_maanden))
    print("")
    print("Maandelijkse betaling is : %.2f" % maandelijks_kosten)

main()

