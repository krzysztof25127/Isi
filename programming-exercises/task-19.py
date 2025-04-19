# 19.Sprawdź czy wyraz bądź zdanie podane przez użytkownika jest palindromem.
def function(x):
    x_new = x.replace(" ","").lower()

    if x_new == x_new[::-1]:
        print("To jest palindrom!")
    else:
        print("To nie jest palindrom!")

if __name__ == "__main__":
    x = input("Wprowadź wyraz lub zdanie do sprawdzenia: ")
    function(x)