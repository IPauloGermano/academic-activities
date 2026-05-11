'''
Escreva um programa que leia um número inteiro positivo (n > 1)
e imprima os seus divisores.
'''

n = int(input("Digite um número inteiro positivo (n > 1): "))
# lê um numero inteiro

if n > 1: # condiçao 
    print(f"Os divisores de {n} são:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
