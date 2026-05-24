# 7. Crie uma matriz 3x3 com números inteiros e mostre
#  a soma de todos os elementos. 

matriz = []
s = 0

for x in range(3):
    l = []

    for n in range(3):
        valor = int(input('Digite um numero: '))
        l.append(valor)
        s = s + valor

    matriz.append(l)
print(matriz)
print(s)