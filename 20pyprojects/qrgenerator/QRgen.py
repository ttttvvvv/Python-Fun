# installeer de python libraries
# maak een functie die een tekst pakt en converteert naar een qr code
# sla op als foto


import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


while True:
    url = input("Geef de link voor de QRCode : ") # geef de link
    generate_qrcode(url) 
    print("")
    print("Succesvol uitgevoerd de qr code staat voor u klaar")
    print("")
    
    keuze = input("Druk op E om te stoppen\n\nEnter om nog een QRCode te genereren\n\nVergeet niet de QRCode van naam te veranderen!\n")

    if keuze == "E" or keuze == "e":
        quit()