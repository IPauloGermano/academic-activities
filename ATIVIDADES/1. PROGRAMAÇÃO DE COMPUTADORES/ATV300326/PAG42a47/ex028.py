n1 = input('Digite um número: ')

try:
    tst = int(n1)
    print(tst * 2)
except:
    try:
        tst2 = float(n1)
        print(tst2 / 2)
    except:
        print('Tipo invalido')