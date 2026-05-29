
def ver():
    rest = ['Fla','MENGO','MENGAO']
    senha = input('Digite uma senha de 6 caracters: ')


    if len(senha) != 6:
        print('Senha tem q ter 6 digitos(nada mais ou menos)')
    elif any(palavra in senha for palavra in rest):
        print('A senha não pode conter palavras proibidas')
    elif senha[-1] == 'A' or 'F':
       print('Nao deve cmc com letra A e nem Terminar com F')
    else: 
         print('Senha correta')

ver()

# ##############     

# def quad():
#     x = int(input('Digite ai: '))
#     y = int(input('Digite ai: '))

#     pr = (2 * x) + (2 * y)
#     print(pr)
# quad()

########

# def lenota():
#     m = 0
#     for x in range(3):
#         nota = int(input('Digite sua nota: '))
#         m += nota

#     m /= 3
#     if m >= 7:
#         print('Aprovado!')
#     else:
#         print('Reprovado!') 
              
# lenota()            

##################


# def calc():
#     conta = input('Digite sua conta: ').replace(' ', '')

#     operadores = ['+', '-', '*', '/']

#     for operador in operadores:
#         if operador in conta:
#             numero1, numero2 = conta.split(operador)

#             numero1 = float(numero1)
#             numero2 = float(numero2)

#             if operador == '+':
#                 resultado = numero1 + numero2

#             elif operador == '-':
#                 resultado = numero1 - numero2

#             elif operador == '*':
#                 resultado = numero1 * numero2

#             elif operador == '/':
#                 if numero2 == 0:
#                     print('Erro: não é possível dividir por zero.')
#                     return

#                 resultado = numero1 / numero2

#             print(f'Resultado: {resultado:g}')
#             return

#     print('Erro: operador inválido.')


# calc()