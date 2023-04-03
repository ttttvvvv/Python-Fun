# een woordenboek die vragen en antwoorden beewaart
# een variabelen die de score bijhoud
# loop door het woordenboek door gebruik te maken van key value pairs
# laat elke vraag zien aan de gebruiker en laat hun andwoorden
# laat correct of fout zien
# laat het resultaat zien

quiz = {
    "question1": {
    "question": "Wat is de hoofdstad van Frankrijk",
    "answer": "Parijs"
    },
    "question2": {
    "question": "Wat is de hoofdstad van Duitsland",
    "answer": "Berlijn"
    },
    "question3": {
    "question": "Wat is de hoofdstad van Italië",
    "answer": "Rome"
    },
     "question4": {
    "question": "Wat is de hoofdstad van Spanje",
    "answer": "Madrid"
    },
     "question5": {
    "question": "Wat is de hoofdstad van Portugal",
    "answer": "Lissabon"
    },
     "question6": {
    "question": "Wat is de hoofdstad van Zwitzerland",
    "answer": "Bern"
    },
     "question7": {
    "question": "Wat is de hoofdstad van Oostenrijk",
    "answer": "Wenen"
    },
}


while True:
    score = 0
    questions = 7
    
    for key, value in quiz.items():
        print(value['question'])
        answer = input("Vul het correcte andwoord in: \n")

        if answer.lower() == value['answer'].lower():
            print("Goed andwoord!")
            score = score + 1
            print(f"Je score is: {str(score)}")
            print("")
            print("")

        else:
            print("Fout, volgende keer beter")
            print("Het andwoord is : " + value['answer'])
            print(f"Je score is: {str(score)}")
            print("")
            print("")

    print("Je hebt " + str(score) + " van de 7 vragen goed ")  
    print("Jou percentage is " + str(int(score/questions * 100)) + "%") 

    Keuze = input("\n\nE voor exit\n\nEnter om opnieuw te spelen\n\n")
    if Keuze == "E" or Keuze == "e":
        print("Programma beëindigd")
        quit()

    
