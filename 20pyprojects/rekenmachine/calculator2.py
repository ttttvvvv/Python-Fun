from secrets import choice

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def min(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print("A. Optellen")
    print("B. Aftrekken")
    print("C. Vermenigvuldigen")
    print("D. Delen")
    print("E. Exit")

    Keuze = input("Keuze: ")

    if Keuze == "A" or Keuze == "a":
        print("Optellen")
        a = float(input("Getal a: "))
        b = float(input("Getal b: "))
        add(a, b)
    elif Keuze == "B" or Keuze == "b":
        print("Aftrekken")
        a = float(input("Getal a: "))
        b = float(input("Getal b: "))
        min(a, b)
    elif Keuze == "C" or Keuze == "c":
        print("Vermenigvuldigen")
        a = float(input("Getal a: "))
        b = float(input("Getal b: "))
        mult(a, b)
    elif Keuze == "D" or Keuze == "d":
        print("Delen")
        a = float(input("Getal a: "))
        b = float(input("Getal b: "))
        div(a, b)
    elif Keuze == "E" or Keuze == "e":
        print("Programma beëindigd")
        quit()


    