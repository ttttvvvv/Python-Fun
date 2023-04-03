# import urllib
# gebruik urllib.request om de data uit de url te halen
# schrijf een functie dat een url lijst opneemt
# return een andwoord
# maak de functie zo dat die het uit een bestand kan lezen

import urllib.request as urllib


def main(url):
    for x in url:
        print("Te checken site:", x)
        
        print("Aan het checken of de site online is....")
        response = urllib.urlopen(x)
        
        print("Site ", x, " is online!")
        print("Het andwoord was:", response.getcode())
        print("")
        print("------------------------------------------------------------------------")
        print("")


        
print("")
print("")
print("")
print("")
print("-------------------------------------------------------")
print("------------------Is Die Site Online-------------------")
print("-------------------------------------------------------")
print("")
print("")




#invoer_url = input("Voer de url in..\n-->")
invoer_url = ["https://www.w3schools.com/", "https://www.google.com/", "https://www.youtube.com/"] #hoe maak ik er een lijst van?, Hoe maak ik de lijst in een file?



main(invoer_url)