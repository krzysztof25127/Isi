# 9. Stwórz klasy Vehicle i Car z polami nazwa, rok_produkcji i przebieg oraz metodami is_old() i is_long_mileage().
# Stwórz po jednym obiekcie dla każdej z klas oraz trzeci obiekt, gdzie klasa Car dziedziczy z klasy Vehicle.
# Dla każdego z obiektów wywołaj obie metody, co najmniej raz użyj dekoratora @property w każdym z trzech przypadków.

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = int(rok_produkcji)
        self.przebieg = int(przebieg)

    @property
    def is_old(self):
        return "Tak" if (2024 - self.rok_produkcji) > 10 else "Nie"
    @property
    def is_long_mileage(self):
        return "Tak" if self.przebieg > 150000 else "Nie"
    def __str__(self):
        return f"({self.nazwa}, Rok:{self.rok_produkcji}, Przebieg:{self.przebieg} km)"

class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg, marka):
        super().__init__(nazwa,rok_produkcji,przebieg)
        self.marka = marka

    def __str__(self):
        return f"({self.nazwa}, Rok:{self.rok_produkcji}, Przebieg:{self.przebieg} km, Marka:{self.marka})"


def main():
    vehicle = Vehicle("Samochód", "2005", "250000")
    car = Car("Samochód", "2005", "250000", "Toyota")
    for obj in [vehicle, car]:
        print(obj)
        print("Czy stary?: ",obj.is_old)
        print("Czy duży przebieg?: ",obj.is_long_mileage)
        print("----------")


if __name__ == "__main__":
    main()