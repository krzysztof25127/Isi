# 10.Napisz program, który korzystająć z metody chr() wygeneruje łańcuch znakowy z alfabetem, czyli 'abc....xyz'.
# Do pliku alfabet1-numeralbumu.txt zapisz wygenerowany łańcuch znakowy, a do pliku alfabet2-numeralbumu.txt zapisz litery z ww. łańcucha znakowego,
# tylko że każda litera ma się znaleźć w osobnej linii w pliku.
# Hint: oprócz funkcji write() skorzystaj również z menadżera kontekstu with, żeby nie zapomnieć o zamknięciu pliku.

def funkcja():

    alfabet = [chr(i) for i in range(97, 123)]

    with open("alfabet1-25127.txt", "w") as plik:
        plik.write("".join(alfabet))
    return alfabet

def funkcja2():
    alfabet = [chr(i) for i in range(97, 123)]

    with open("alfabet2-25127.txt", "w") as plik:
        for litera in alfabet:
            plik.write(litera +"\n")


if __name__ == '__main__':
    funkcja2()