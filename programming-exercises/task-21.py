# Dziedziczenie klas. Klasa Animal ma zawierać atrybuty takie jak name, age, sex oraz metodę sound(). 
# Klasy Dog, Cat oraz Fox dziedziczą po klasie Animal oraz nadpisują funkcje sound() odpowiednimi dźwiękami, dodatkowo klasy Dog oraz Cat posiadają atrybut breed.

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        return "Dzwiek zwierzęcia"
    

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Hau Hau"

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Miau"

class Fox(Animal):
    def sound(self):
        return "Sss"


dog = Dog("Andrzej", 5, "M", "Owczarek")
cat = Cat("Tobiasz", 3, "M", "Perski")
fox = Fox("Lisek", 2, "F")

print(dog.sound())
print(cat.sound())
print(fox.sound())