# 20. Prosta gra, program generuje losową liczbę od 1 do 100, użytkownik ma odgadnąć liczbę, jeżeli nie trafi, ma zostać wyświetlona podpowiedź czy za duża czy za mała liczba.
import random

def function():
    liczba = random.randint(1,100)
    proba = 0
    print("Zgadnij liczbę z przedziału od 1 do 100!")

    while True:
        try:
            zgadnij = int(input("Podaj liczbę: "))
            proba += 1

            if zgadnij < liczba:
                print("Za mała liczba!")
            elif zgadnij > liczba:
                print("Za duża liczba!")
            else:
                print(f"Brawo! Zgadłeś! Ilość prób: {proba}.")
                break
        except ValueError:
            print("Podaj poprawną liczbę całkowitą!")

if __name__ == "__main__":
    function()