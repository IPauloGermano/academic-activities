

# n = int(input('Numero de mtrix: '))
# m = int(input('Numero de elementos; '))
# mtrix = []
# for i in range(n):
#     mtrix.append([0] * m)
# # print(mtrix) # imprime a matriz toda
# for i in range(n): # imprime cada linha da matriz
#     print(mtrix[i])

# # Mtrix 3x3 digitada pelo usuario e conta quantos numeros pares tem na mtrix (Com menos linhas possivel)

# mtrix = []
# for i in range(3):
#     mtrix.append([0] * 3)
# for i in range(3):
#     for j in range(3):
#         mtrix[i][j] = int(input(f'Elemento [{i}][{j}]: '))
# pares = 0
# for i in range(3):
#     for j in range(3):
#         if mtrix[i][j] % 2 == 0:
#             pares += 1
# print(f'Quantidade de numeros pares: {pares}')

############################

# # Length (len) - quantidade de elementos em uma lista

# mtrix = ([[1, 2, 3],[4, 5, 6]])

# print(len(mtrix)) # quantidade de linhas
# print(len(mtrix[0])) # quantidade de colunas

# ###################################################
# # Tuplas - imutaveis, nao podem ser alteradas depois de criadas
# v = ('a', 'b', 'c', 'd', 'e')
# v[1]='E' 
# print(v)

#################################

# # Dicionarios 

# dados_clientes = {
#     'nome': 'Joao',
#     'Endereco': 'Rua 1',
#     'Telefone': '123456789'}
# print(dados_clientes['nome']) # Acessa o valor da chave 'nome'
# dados_clientes['Telefone'] = '987654321' # Altera o valor da chave 'Telefone'
# print(dados_clientes['Telefone'])
# dados_clientes.pop('Endereco') # Remove a chave 'Endereco' e seu valor
# print(dados_clientes)

###########################

# # String

# nome = 'Joao Silva'

# if nome.startswith('Joao'):
#     print('O nome começa com Joao')
# elif nome.endswith('Silva'):
#     print('O nome termina com Silva')

##############################

# frase = 'Python é uma linguagem de programação poderosa e fácil de aprender.'

# posicao = frase.find('programação')

# if posicao != -1:
#     print(f'A palavra "programação" foi encontrada na posição {posicao}.')
# else:
#     print('A palavra "programação" não foi encontrada na frase.')

    ####################################


