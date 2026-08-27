# Menu Interativo de Operações com Listas
while True:
    print("1 - Maior/Menor 2 - Pares/Ímpares 3 - Busca 4 - Remoção 5 - Contagem 6 - Listas 7 - Produtos"\
    " 8 - Ordem/Contagem 0 - Sair")
    op = input("Opção: ")

    # Opção Sair
    if op == "0":
        print('FIM')
        break

    # Opção Maior/Menor
    elif op == "1":
        l = []
        for x in range(10):
            usr = int(input('Digite um número: '))
            l.append(usr)
        print(l)
        print(f'Maior valor: {max(l)}')
        print(f'Menor valor: {min(l)}')

    # Opção Pares/Ímpares
    elif op == "2":
        lp = []
        li = []
        for x in range(15):
            usr = int(input('Digite um número: '))
            if usr % 2 == 0:
                lp.append(usr)
            else:
                li.append(usr)
        print(f'Pares: {lp}')
        print(f'Ímpares: {li}')

    # Opção Busca
    elif op == '3':
        l = []
        for x in range(8):
            usr = int(input('Digite um número: '))
            l.append(usr)

        v = int(input('Verifique se está presente na lista: '))

        if v in l:
            print(f'{v} está presente na lista!')
        else:
            print(f'{v} não está presente na lista!')

    # Opção Remoção 
    elif op == '4':
        l = []
        for x in range(10):
            usr = int(input('Digite um número: '))
            l.append(usr)

        num = int(input('Digite o número para remover: '))

        if num in l:
            while num in l:
                l.remove(num)
            print('Lista atualizada:', l)
        else:
            print('Número não encontrado na lista.')

    # Opção Contagem
    elif op == '5':
        l = []
        p = 0
        n = 0
        z = 0

        for x in range(20):
            usr = int(input('Digite um número: '))
            l.append(usr)

            if usr > 0:
                p += 1
            elif usr < 0:
                n += 1
            else:
                z += 1

        print(f'Números positivos: {p}\nNegativos: {n}\nZeros: {z}')

    # Opção Listas
    elif op == "6":
        l1 = []
        l2 = []

        for i in range(5):
            l1.append(int(input("l1: ")))

        for i in range(5):
            l2.append(int(input("l2: ")))

        print("\nComuns:", end=" ")
        for x in l1:
            if x in l2:
                print(x, end=" ")

        print("\nSó l1:", end=" ")
        for x in l1:
            if x not in l2:
                print(x, end=" ")

        print("\nSó l2:", end=" ")
        for x in l2:
            if x not in l1:
                print(x, end=" ")

    # Produtos
    elif op == "7":
        nomes = []
        precos = []
        estoque = []

        for i in range(5):
            nomes.append(input("Nome do produto: "))
            precos.append(float(input("Preço do produto: ")))
            estoque.append(int(input("Quantidade em estoque: ")))

        print("\nProdutos com estoque menor que 10:")
        for i in range(5):
            if estoque[i] < 10:
                print(nomes[i], end=" ")

        maior = precos[0]
        pos = 0

        for i in range(5):
            if precos[i] > maior:
                maior = precos[i]
                pos = i

        print(f"\n\nProduto mais caro: {nomes[pos]} - {maior}")
    
    # Opção Ordem/Contagem
    elif op == "8":
        l = []
        par = 0
        impar = 0

        for i in range(12):
            l.append(int(input("Digite um número: ")))

            if l[i] % 2 == 0:
                par += 1
            else:
                impar += 1

        crescente = l[:]
        decrescente = l[:]

        crescente.sort()
        decrescente.sort(reverse=True)

        print("\nLista em ordem crescente:", crescente)
        print("Lista em ordem decrescente:", decrescente)

        print(f"\nPares: {par}")
        print(f"Ímpares: {impar}")

    else:
        print('Opção inválida!')