lista = []

# Leitura dos 30 valores positivos
for i in range(30):
    valor = int(input(f"Digite o {i+1}º valor positivo: "))
    lista.append(valor)

# Encontrando o menor valor
menor = min(lista)

# Contando quantos são divisíveis pelo menor valor
quantidade = 0

for numero in lista:
    if numero % menor == 0:
        quantidade += 1

# Resultados
print("Menor valor da lista:", menor)
print("Quantidade de elementos divisíveis pelo menor valor:", quantidade)