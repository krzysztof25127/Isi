# 6. Napisz program, który tworzy słownik o nazwie zawierającej Twój numer albumu.
# Kluczami powinny być liczby od 10 do 20, a wartościami pseudolosowe łańcuch znaków o długości 8.
# Hint: skorzystaj z modułów string i random.
import random
import string

def tworzslownik():
    slownik_25127 = {}

    for i in range(10, 21):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        slownik_25127[i] = random_string
    return slownik_25127

if __name__ == '__main__':

    print(tworzslownik())