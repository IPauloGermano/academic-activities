n1 = int(input('Digite um número: '))

try:
    tst = int(n1)
    if tst % 2 == 0:
        if tst > 100:
            print('Par alto')
        else:
            print('Par baixo')
    else:
        print('Impar')
except:
    print("Entrada inválida")