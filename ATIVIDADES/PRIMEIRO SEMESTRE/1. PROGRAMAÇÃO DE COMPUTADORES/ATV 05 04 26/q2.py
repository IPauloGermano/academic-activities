'''
Escreva um programa que leia um número inteiro positivo (n > 1)
e imprima o número de seus divisores
'''

n = int(input('xd: '))
c = 0

if n > 0:
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

print(c)