for i in range(3):
    nome = input("Informe o nome da pessoa: ")
    telefone = input("Informe o telefone da pessoa: ")
    nome_arquivo = input("Informe o nome do arquivo: ")

    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"

    arquivo = open(nome_arquivo, "w")
    arquivo.write(nome + "\n")
    arquivo.write(telefone + "\n")
    arquivo.close()

    print("Contato cadastrado com sucesso!")