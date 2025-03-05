# 1. Napisz program (na dwa sposoby), który sprawdza czy wczytany pojedynczy znak jest cyfrą lub nie.
#    Jeśli wczytamy więcej znaków, należy wziąć tylko pierwszy.
#    Hint: skorzystaj z funkcji isdigit() i isinstance().

#WERSJA isdigit()
def czyCyfra(x):
    if x.isdigit():
        return ("Znak jest liczbą")
    else:
        return ("Znak nie jest liczbą!")

#WERSJA isinstance()
def czyJestTypem(x):
    try:
        x = int(x)
        if isinstance(x,int):
            return ("Znak jest liczbą!")
    except ValueError:
        return ("Znak nie jeset liczbą!")


if __name__ == '__main__':
    x = input('Podaj znak: ')[0]
    print(f"Funkcja isdigit(): {czyCyfra(x)}")
    print(f"Funkcja isinstance(): {czyJestTypem(x)}")

