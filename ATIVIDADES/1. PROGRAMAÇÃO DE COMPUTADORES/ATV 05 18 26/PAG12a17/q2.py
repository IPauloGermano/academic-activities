mtrix = []
menor_idade = None
nome_mais_novo = ''

for x in range(10):
    nm = input('Digite o nome: ')
    age = int(input('Digite a idade: '))

    mtrix.append([nm, age])

    if menor_idade is None or age < menor_idade:
        menor_idade = age
        nome_mais_novo = nm

print(f'A pessoa mais nova é {nome_mais_novo}, com {menor_idade} anos.')