'''
Faça um programa que leia a distância percorrida e o tempo gasto por um atleta,
calcule a velocidade média (velocidade = distância / tempo) e pergunte se...
o usuário deseja continuar (sim ou nao). O programa deve repetir até que seja digitado "nao".
'''

continuar = "sim"

while "s" in continuar:
    distancia = float(input("Digite a distância percorrida (Km): "))
    tempo = float(input("Digite o tempo gasto (horas): "))

    velocidade = distancia / tempo

    print(f"Velocidade média: {velocidade} Km/h")

    continuar = input("Deseja continuar? (sim/nao): ").lower()

print("Programa encerrado.")

    