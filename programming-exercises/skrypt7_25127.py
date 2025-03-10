from utils.obliczenia import potega, pierwiastek, sinus, wartosc_bezwzgledna
import math
def funkcja():
    print("3 do potęgi 9:", potega(3,6))
    print("Pierwiastek z 256:", pierwiastek(256))
    print("Sinus z PI/2:", sinus(math.pi/2))
    print("Wartość bezwzględna dla -534:", wartosc_bezwzgledna(-534))


if __name__ == '__main__':
    funkcja()