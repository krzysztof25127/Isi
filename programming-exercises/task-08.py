# 8. Napisz program, który generuje losowy ciąg znaków o długości 100, a następnie utwórz słownik którego kluczami będą unikalne znaki występujące w ciągu, a wartościami liczba ich wystąpień w ciągu znakowym.
# Utwórz listę, której każdy element to krotka (tupla), zawierająca kolejny klucz z ww. słownika i odpowiadającą mu wartość liczbową.
# Hint: skorzystaj z modułu collections i klasy Counter().

import random
import string
from collections import Counter

def generuj():
    losowy_ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    zlicz = Counter(losowy_ciag)
    zlicz_lista = list(zlicz.items())
    return losowy_ciag, zlicz, zlicz_lista

if __name__ == '__main__':
    losowy_ciag, zlicz, zlicz_lista = generuj()

    print("Losowy ciąg: ")
    print(losowy_ciag)
    print("\nZliczone znaki:")
    print(zlicz)
    print("\nLista: ")
    print(zlicz_lista)