# Calculadora Simples com Funções

def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            return "Erro: divisão por zero"
        return num1 / num2
    else:
        return "Operação inválida"


num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
operador = input("Informe a operação (+, -, *, /): ")

resultado = calculadora(num1, num2, operador)

print("Resultado:", resultado)