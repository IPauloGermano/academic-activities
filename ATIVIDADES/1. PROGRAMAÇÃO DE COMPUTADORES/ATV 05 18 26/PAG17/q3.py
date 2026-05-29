''' matriz 3x3 de inteiros e multiplique os elementos da diagonal 
principal da matriz por um número k. Imprima a matriz na tela antes 
e depois da multiplica•ção.'''

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um valor: ")))
    matriz.append(linha)

k = int(input("Digite k: "))

print("Matriz antes:")
for i in range(3):
    print(matriz[i])

matriz[0][0] = matriz[0][0] * k
matriz[1][1] = matriz[1][1] * k
matriz[2][2] = matriz[2][2] * k

print("Matriz depois:")
for i in range(3):
    print(matriz[i])