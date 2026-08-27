n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 != n2:
    if n1 > n2:
        print(f'A diferença entre {n1} e {n2} é: {n1 - n2}')
    else:
        print(f'A diferença entre {n1} e {n2} é: {n2 - n1}')