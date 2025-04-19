# 17. Stwórz klasę o nazwie Dog, która będzie posiadała zmienne takie jak: name, age, coat_color.
# Dodatkowo klasa posiada funkcje sound(), po wywołaniu której wypisywany jest tekst: {name} is barking!
# Stworzyć 3 obiekty klasy Dog.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = int(age)
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!")

def function():
    dog1 = Dog("Max", 10, "brown")
    dog2 = Dog("Bella", 10, "black")
    dog3 = Dog("Jim", 10, "beige")

    dog1.sound()
    dog2.sound()
    dog3.sound()


if __name__ == "__main__":
    function()