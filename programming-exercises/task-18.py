# 18.Stworzyć plik funkcje.py, w którym należy zaimplementować funkcję: dodawanie, odejmowanie, dzielenie, mnożenie oraz modulo.
# W pliku main.py zaimportować plik funkcje.py i wykorzystać zaimportowane funkcje na przykładowych wartościach.

from utils.funkcje import dodawanie, odejmowanie, dzielenie, mnozenie, modulo
def funkcja(x,y):
    print("Dodawanie:", dodawanie(x,y))
    print("Odejmowanie:", odejmowanie(x,y))
    print("Dzielenie:", dzielenie(x,y))
    print("Mnozenie:", mnozenie(x,y))
    print("Modulo: ", modulo(x,y))


if __name__ == '__main__':
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    funkcja(x,y)