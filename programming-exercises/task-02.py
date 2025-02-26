print('Podaj ciąg znaków:')
x = input()
if len(x) < 2:
    print('Co najmniej dwa znaki!')
    x = input()
print('Twój ciąg to:'+x)