n1 = int(input('Digite um número: '))

if n1 > 0 and n1 < 10:
    print('Pequeno')
elif n1 >= 10 and n1 < 100:
    print('Médio')
elif n1 > 100:
    print('Grande')
else:
    print('Negativo ou zero')