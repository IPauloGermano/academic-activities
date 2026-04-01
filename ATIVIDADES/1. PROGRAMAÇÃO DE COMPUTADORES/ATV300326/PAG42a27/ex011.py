n1 = int(input('Digite um número: '))

if n1 % 2 == 0:
    if n1 < 0:
        print('Par negativo')
    else:
        print('Par positivo')
else:
    print('Impar')