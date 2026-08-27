lista = []

# Leitura dos números positivos
while True:
    num = int(input("Digite um número positivo: "))

    if num <= 0:
        break

    lista.append(num)

# Número a ser verificado
x = int(input("Digite o valor de x: "))

# Verificação
if x in lista:
    print(f"{x} pertence à lista.")
else:
    print(f"{x} não pertence à lista.")