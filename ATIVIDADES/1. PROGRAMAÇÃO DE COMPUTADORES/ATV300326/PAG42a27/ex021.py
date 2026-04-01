n1 = int(input('Digite um número: '))

if n1 > 0:
    if (n1 % 2 == 0) and (n1 % 3 == 0):
        print("Múltiplo de 2 e 3")
    else:
        print('Não atende')
else:
    print('Número inválido')