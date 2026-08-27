'''
1)
nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print("Nota válida:", nota)'''
#######################################################

'''
2)
nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print("Nota válida:", nota)'''
########################################################
'''
3)
n = int(input("Digite um número inteiro positivo: "))

while n <= 0:
    print("Número inválido.")
    n = int(input("Digite um número inteiro positivo: "))

contador = 1

while contador <= n:
    print(contador)
    contador = contador + 1
'''
############################################################
'''
4)
soma = 0

numero = int(input("Digite um número: "))

while numero >= 0:
    soma = soma + numero
    numero = int(input("Digite outro número: "))

print("Soma total:", soma)

'''
#############################################################
'''
5)
numero = int(input("Digite um número: "))

while numero != 0:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    numero = int(input("Digite outro número: "))

print("Programa encerrado.")

'''
##############################################################
'''
6)
numero = int(input("Digite um número: "))

maior = numero

while numero != 0:
    if numero > maior:
        maior = numero

    numero = int(input("Digite outro número: "))

print("Maior número digitado:", maior)
'''
#####################################################
'''
7)
soma = 0
quantidade = 0

nota = float(input("Digite uma nota: "))

while nota != -1:
    if nota >= 0 and nota <= 10:
        soma = soma + nota
        quantidade = quantidade + 1
    else:
        print("Nota inválida.")

    nota = float(input("Digite outra nota: "))

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
else:
    print("Nenhuma nota válida foi digitada.")
'''
#######################################################
'''
8)
numero = int(input("Digite um número: "))

contador = 1

while contador <= 10:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador = contador + 1

'''
#########################################################
'''
9)
positivos = 0
negativos = 0

numero = int(input("Digite um número: "))

while numero != 0:
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

    numero = int(input("Digite outro número: "))

print("Quantidade de positivos:", positivos)
print("Quantidade de negativos:", negativos)

'''
###########################################################
'''
10)
numero_correto = 7

palpite = int(input("Adivinhe o número: "))

while palpite != numero_correto:
    if palpite > numero_correto:
        print("O palpite é maior que o número correto.")
    else:
        print("O palpite é menor que o número correto.")

    palpite = int(input("Tente novamente: "))

print("Você acertou!")

'''