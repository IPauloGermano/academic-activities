# 6. Crie uma matriz 3x3 preenchida pelo usuário
# e exiba todos os valores na tela.

matriz = []

for x in range(3):
    l = []

    for n in range(3):
        valor = int(input('Digite um numero: '))
        l.append(valor)

    matriz.append(l)
print(matriz)