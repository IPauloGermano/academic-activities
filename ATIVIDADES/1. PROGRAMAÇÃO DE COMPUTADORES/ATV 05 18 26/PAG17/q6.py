# Identificação da Linha com Maior Soma em Matriz 3x3

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um valor: ")))
    matriz.append(linha)

maior_soma = 0
maior_linha = 0

for i in range(3):
    soma = 0
    for j in range(3):
        soma = soma + matriz[i][j]

    if i == 0 or soma > maior_soma:
        maior_soma = soma
        maior_linha = i

print("Matriz:")
for i in range(3):
    print(matriz[i])

print("Linha de maior soma:", matriz[maior_linha])
print("Soma:", maior_soma)