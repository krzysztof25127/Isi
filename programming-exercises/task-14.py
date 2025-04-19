# 14. Używając pętli, wyświetl liczby w przedziale od 1 do 100 podzielne przez 3 i 4 oraz podaj ich liczbę.
def function():
    liczba = 0
    for i in range(1,101):
        if(i % 3 == 0) and (i % 4 == 0):
            print(i)
            liczba += 1
    print("Liczba liczb podzielnych przez 3 i 4: ", liczba)

if __name__ == "__main__":
    function()