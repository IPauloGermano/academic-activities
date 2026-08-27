# Programa que le 30 num int e armazena em uma lista. e calcule e imprima: a) menor valor da lista; b) a quantidade de elementos que sao divisiveis pelo menor valor;

l = []
for i in range(30):
    n = int(input("Digite um número inteiro: "))
    l.append(n)
menor = min(l)
print("Menor valor da lista:", menor)
contador = 0
for num in l:
    if num % menor == 0:
        contador += 1
print("Quantidade de elementos divisíveis pelo menor valor:", contador)
