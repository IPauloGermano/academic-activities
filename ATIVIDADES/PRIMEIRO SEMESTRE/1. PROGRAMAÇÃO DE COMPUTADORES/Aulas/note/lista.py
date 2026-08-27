# letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',]
# print(letra[::2]) # Apenas posicoes pares
# print(letra[0:3]) # Os 3 primeiros elementos
# print(letra[::-1]) # Invertendo a ordem da lista

# lista = [1, 2, 3, 4, 5, 6, 7, 8]
# lista[2:4] = ["A", "B"] # Substituindo os elementos 3 e 4 por A e B
# print(lista)
# lista[2:4] = [] # Removendo os elementos 3 e 4
# print(lista)

# animais = [] # Criando uma lista vazia
# animais.append("Cachorro") # Append adiciona um elemento ao final da lista
# print(animais)
# animais.append("Gato")
# print(animais)
# animais.append("Pássaro")
# print(animais)

# frutas = ["Maçã", "Banana", "Laranja",]
# frutas.insert(1, "Abacaxi") # Insert adiciona um elemento em uma posição específica
# print(frutas)
# frutas.insert(len(frutas), "Uva") # Adicionando um elemento no final da lista usando insert
# # P q serve o len(frutas)?

# print(frutas)

# INDEX 
# cinema = ["Sony Pictures", "Warner Bros", "Universal Pictures", "Paramount Pictures", "20th Century Fox"]
# print(cinema.index("Warner Bros")) # Retorna o índice do elemento "Warner Bros"
# print(cinema.index("Disney")) # ValorError: 'Disney' is not in list, pois o elemento "Disney" não está presente na lista cinema.

# REMOVE
# cinema.remove("Universal Pictures") # Remove o elemento "Universal Pictures" da lista cinema
# print(cinema)

# POP 
# cinema.pop(1) # Remove o elemento na posição 1 (Warner Bros) da lista cinema
# print(cinema)
# diferente do remove, o pop retorna o elemento removido, 
# então podemos armazenar esse valor em uma variável

# count
# cinema.append("Sony Pictures") # Adicionando "Sony Pictures" novamente para testar o count
# print(cinema)
# print(cinema.count("Sony Pictures")) # Retorna o número de vezes que "Sony Pictures" aparece na lista cinema

# sort

a = [5, 2, 9, 1, 5, 6]
a.sort()
print(a)
a.sort(reverse=True) # Ordena a lista a em ordem decrescente
print(a)