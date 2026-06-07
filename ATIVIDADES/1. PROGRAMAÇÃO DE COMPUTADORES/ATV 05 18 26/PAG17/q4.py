# Soma de Matrizes 2x2

A = []
B = []
C = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor de A: ")))
    A.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor de B: ")))
    B.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)

print("Matriz C:")
for i in range(2):
    print(C[i])