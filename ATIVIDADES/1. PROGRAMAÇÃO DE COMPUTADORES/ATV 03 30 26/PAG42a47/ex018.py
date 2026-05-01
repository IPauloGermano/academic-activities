n1 = int(input('Digite um número: '))

if n1 == 0:
    print('neutro')

elif n1 % 2 == 0 and n1 > 0:
    print('Par positivo')

elif n1 % 2 == 0 and n1 < 0:
    print('Par negativo')

elif n1 % 2 != 0 and n1 > 0:
    print('Impar positivo')

else:
    print('Impar negativo')