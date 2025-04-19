# 12. Zamienić wszystkie litery o na 0, e na 3, i na 1,a na 4 w podanej przez użytkownika sentencji.


def function(zdanie):
    zdanie = zdanie.replace("o", "0")
    zdanie = zdanie.replace("e", "3")
    zdanie = zdanie.replace("i", "1")
    zdanie = zdanie.replace("a", "4")
    return zdanie

if __name__ == "__main__":
    zdanie = input("Podaj sentencję: ")
    print(function(zdanie))