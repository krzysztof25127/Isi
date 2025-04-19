# 16. Napisz prostą funkcję o nazwie potega(), przyjmującą jeden argument, podnoszącą podaną liczbę do trzeciej potęgi.



def potega(x):
    x = pow(x,3)
    return x


if __name__ == "__main__":
    x = int(input("Podaj liczbę, którą podnieść do trzeciej potęgi: "))
    wynik = potega(x)
    print("Wynik:",wynik)