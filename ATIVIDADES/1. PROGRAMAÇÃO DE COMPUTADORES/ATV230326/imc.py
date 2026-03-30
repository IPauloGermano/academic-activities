# 3E

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (cm): '))

altura = altura / 100  

imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')