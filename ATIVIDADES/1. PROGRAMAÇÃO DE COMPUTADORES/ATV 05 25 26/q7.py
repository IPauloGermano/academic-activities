nome_arquivo = input("Informe o nome do arquivo a ser lido: ")

if not nome_arquivo.endswith(".txt"):
    nome_arquivo += ".txt"

try:
    arquivo = open(nome_arquivo, "r")

    nome = arquivo.readline()
    telefone = arquivo.readline()

    arquivo.close()

    print("Nome:", nome)
    print("Telefone:", telefone)

except FileNotFoundError:
    print("Arquivo não encontrado!")