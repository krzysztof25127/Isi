# 2. Napisz program, który sprawdza czy wczytany łańcuch znakowy jest liczbą lub nie.
#    Muszą być wczytane co najmniej dwa znaki.
#    Hint: skorzystaj z funkcji all().


def sprawdz(x):
    return all(c.isdigit() for c in x)

if __name__ == '__main__':
    x = input('Podaj łańcuch znaków: ')
    while len(x)<2:
        print("Muszą być conajmniej dwa znaki!")
        x = input('Podaj łańcuch znaków: ')
    if sprawdz(x):
        print("Podany ciąg jest liczbą")
    else:
        print("Podany ciąg NIE jest liczbą")