valor = input("Digite um valor: ")

print("Tipo da variável:", type(valor))

try:
    numero = float(valor)
    resultado = numero / 2
    print("Resultado da divisão por 2:", resultado)
except:
    print("Não numérico")