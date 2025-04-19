# 13. Używając pętli, wyświetl liczby w przedziale od 1 do 50 oprócz liczb podzielnych przez 3.

def funkcja():
    for i in range(1, 51):
        if i % 3 != 0:
            print(i)

if __name__ == "__main__":
    funkcja()