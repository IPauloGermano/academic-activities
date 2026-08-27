# 8. . Leia uma matriz 4x4 e informe qual é o maior 
# número armazenado nela.

matriz = []
maxi = 0

for x in range(4):
    l = []

    for n in range(4):
        valor = int(input('Digite um numero: '))
        l.append(valor)
        if valor > maxi:
            maxi = valor

    matriz.append(l)
print(f'Maior numero: {maxi}')
print(matriz)