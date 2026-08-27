# Multiplicação de Matrizes

la = int(input("Linhas de A: "))
ca = int(input("Colunas de A: "))
lb = int(input("Linhas de B: "))
cb = int(input("Colunas de B: "))

A = []
for i in range(la):
    linha = []
    for j in range(ca):
        linha.append(int(input("Valor de A: ")))
    A.append(linha)

B = []
for i in range(lb):
    linha = []
    for j in range(cb):
        linha.append(int(input("Valor de B: ")))
    B.append(linha)

print("Matriz A:")
for i in range(la):
    print(A[i])

print("Matriz B:")
for i in range(lb):
    print(B[i])

if ca == lb:
    C = []
    for i in range(la):
        C.append([0] * cb)

    for i in range(la):
        for j in range(cb):
            for k in range(ca):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    print("Matriz C:")
    for i in range(la):
        print(C[i])
else:
    print("Não é possível multiplicar.")