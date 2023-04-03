def main():
    print(" Welkom bij email slicer ")
    print("")

    email_input = input("Voer je email adres in:  ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Gebruikersnaam is: {username}")
    print(f"Domein is: {domain}")
    print(f"Extension is: {extension}")


main()

