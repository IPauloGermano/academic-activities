n1 = int(input('Digite um número: '))

if n1 % 5 == 0:
    if n1 > 50:
        print('Múltiplo alto')
    else:
        print('Múltiplo baixo')
else:
    print('Não é múltiplo')