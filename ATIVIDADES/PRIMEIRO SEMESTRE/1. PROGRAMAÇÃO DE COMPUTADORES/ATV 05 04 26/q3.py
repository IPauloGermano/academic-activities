'''Escreva um programa que leia diversos números inteiros
positivos e exiba o dobro de cada um. A leitura deve ser
interrompida quando for digitado um número negativo. 
'''
while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        print('FIM')
        break
    else:
        print(f'O dobro de {n} é {n * 2}')
        