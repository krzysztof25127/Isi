# 15. Używając pętli, dodawaj do wcześniej zadeklarowanej tabeli liczby z przedziału od 1 do 100, które są podzielne przez 3 lub podzielne przez 5.
def function():
    x = []
    for i in range(1,101):
        if i % 3 == 0 or i % 5 == 0:
            x.append(i)
    print(x)

if __name__ == "__main__":
    function()