lista = []

# Leitura dos 7 valores
for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista.append(valor)

# Exibindo em ordem inversa
print("Valores em ordem inversa:")

for i in range(6, -1, -1):
    print(lista[i])