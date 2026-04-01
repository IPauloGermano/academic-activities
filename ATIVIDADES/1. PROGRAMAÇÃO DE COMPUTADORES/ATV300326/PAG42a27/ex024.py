n1 = int(input('Digite um número: '))

if n1 > 0 or n1 < 100:
    if n1 % 2 == 0:
        p = 'Par no intervalo'
elif n1 % 3 == 0:
    i = 'Impar no intervalo'

else: 
    print('Fora do intervalo')
