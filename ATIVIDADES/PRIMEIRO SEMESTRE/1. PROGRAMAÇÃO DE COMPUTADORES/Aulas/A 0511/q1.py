np = int(input('Digite um número inteiro: '))
lista = []

while True:
    if np > 0:
        np = int(input('Digite um número inteiro: '))
        lista.append(np)
    else:
        break
    
x = int(input('Verifique se o número está na lista: '))
if x in lista:
    print(f'O número {x} está na lista.')
else:
    print(f'O número {x} não está na lista.')
