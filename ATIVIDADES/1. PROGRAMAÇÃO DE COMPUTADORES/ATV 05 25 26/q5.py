def media(num1, num2):
    return (num1 + num2) / 2


def diferenca_maior_menor(num1, num2):
    if num1 > num2:
        return num1 - num2
    return num2 - num1


def produto(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2


num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print("""
Escolha uma opção:

1 - Média entre os números
2 - Diferença do maior pelo menor
3 - Produto entre os números
4 - Divisão do primeiro pelo segundo
""")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print("Resultado:", media(num1, num2))
elif opcao == 2:
    print("Resultado:", diferenca_maior_menor(num1, num2))
elif opcao == 3:
    print("Resultado:", produto(num1, num2))
elif opcao == 4:
    print("Resultado:", divisao(num1, num2))
else:
    print("Opção inválida!")