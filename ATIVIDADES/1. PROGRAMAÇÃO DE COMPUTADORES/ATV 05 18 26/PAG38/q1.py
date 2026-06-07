# 1. Crie um programa que receba uma palavra e mostre quantas vogais existem nela.

p = input('Digite uma palavra: ').lower() 
# Recebe uma palavra e converte suas letras para minúsculas.

vogais = ['a','e','i','o','u'] # Lista com as vogais que serão verificadas.
c = 0 # Contador de vogais encontradas.

for letra in p: # Percorre cada letra da palavra digitada.
    if letra in vogais: # Verifica se a letra atual é uma vogal.
        c += 1 # Incrementa o contador ao encontrar uma vogal.

print(f'A palavra "{p}" tem {c} vogais')