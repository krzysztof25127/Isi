# 11.Odwrócić sentencję podaną przez użytkownika.

def function():
    zdanie = input("Podaj sentencję do odwrócenia: ")
    odwrocone = zdanie[::-1] #[start:stop:step]
    return odwrocone

if __name__ == '__main__':
    print(function())