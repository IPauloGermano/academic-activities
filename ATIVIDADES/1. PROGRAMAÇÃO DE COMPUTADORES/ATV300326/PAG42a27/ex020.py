n1 = int(input('Digite um número: '))

if n1 < 0 or n1 > 100:
    print(n1)
    print(f'{n1} está fora do intervalo')
else:
    print(f'{n1} está dentro do intervalo')