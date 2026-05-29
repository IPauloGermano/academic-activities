matrix = []
c = 0

for linha in range(3):
    l = []

    for coluna in range(3):
        valor = int(input('Digite um numero: '))
        l.append(valor)
        if valor % 2 == 0:
            c += 1
    matrix.append(l)
print(f'Tem {c} numero pares!')
print(matrix)