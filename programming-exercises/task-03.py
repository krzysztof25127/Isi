# 3. Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeks pierwszego wystąpienia ciągu lub -1, gdy nie ma takiego ciągu.
#    Hint: skorzystaj z funkcji find().


def szukaj(txt, ciag):
    return txt.find(ciag)



if __name__ == '__main__':
    txt = input('Podaj łańcuch znaków: ')
    ciag = input('Podaj ciąg, którego szukasz: ')

    indeks = szukaj(txt, ciag)

    if indeks != -1:
        print(f'Znaleziono ciąg na indeksie: {indeks}')
    else:
        print(f'Nie znaleziono ciągu: {indeks}')