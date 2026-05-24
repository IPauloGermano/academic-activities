#3. Faça um programa que verifique se uma palavra é um palíndromo 
# (ex.: “arara”). 

p = input('Digite uma palavra: ')
i = p[-1::-1]

if p == i:
    print('Palíndromo')
else:
    print('Não é um palíndromo')