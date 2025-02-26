# 1. Napisz program (na dwa sposoby), który sprawdza czy wczytany pojedynczy znak jest cyfrą lub nie.
#    Jeśli wczytamy więcej znaków, należy wziąć tylko pierwszy.
#    Hint: skorzystaj z funkcji isdigit() i isinstance().

# WERSJA isdigit()
# if x.isdigit():
#     print('Znak jest liczbą!')
# else:
#     print('Znak nie jest liczbą!')

#WERSJA isinstance()

x = input()
x = x[0]
try:
    x = int(x)
    if isinstance(x,int):
        print('Znak jest liczbą!')
except ValueError:
    print('Znak nie jest liczbą!')

def czyCyfra(x):



if __name__ == '__main__':
    x = input('Podaj znak: ')[0]

