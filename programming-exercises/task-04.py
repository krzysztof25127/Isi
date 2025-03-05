# 4. Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeksy wszystkich wystąpień ciągu lub -1, gdy nie ma takiego ciągu.
#    Hint: skorzystaj z funkcji split().

def szukaj(txt, ciag):
    indeksy = []
    start = 0
    while start < len(txt):
        indeks = txt.find(ciag, start)
        if indeks == -1:
            break
        indeksy += [i for i in range(indeks, indeks + len(ciag))]
        start = indeks + 1
    return indeksy if indeksy else [-1]

if __name__ == '__main__':
    txt = input('Podaj łańcuch znaków: ')
    ciag = input('Podaj ciąg, którego szukasz: ')

    indeksy = szukaj(txt,ciag)
    print(f'Indeksy wystąpień: {indeksy}')