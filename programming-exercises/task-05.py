# 5. Napisz program (na dwa sposoby), który szuka pierwiastków liczb od 1 do 256 (włącznie) podzielnych bez reszty przez 2.
# Hint: skorzystaj z modułu math i z tzw. 'list comprehensions'.
import math

def szukaj(r1,r2):
    liczby = list(range(r1,r2))
    wyniki = []

    for x in liczby:
        if math.sqrt(x) % 2 == 0:
            wyniki.append(x)
    return wyniki

if __name__ == "__main__":
    r1 = 1
    r2 = 257

    wyniki1 = szukaj(r1,r2)

    wyniki2 = [x for x in range(1, 257) if math.sqrt(x).is_integer() and math.sqrt(x) % 2 == 0]
    print(wyniki1)
    print(wyniki2)
