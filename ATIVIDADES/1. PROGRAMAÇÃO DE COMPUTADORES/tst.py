while True:
    print("\n1-Maior/Menor  2-Pares/Ímpares  3-Busca  4-Contagem  5-Listas  6-Produtos  7-Tabuada  0-Sair")
    op = input("Opção: ")

    if op == "0":
        break

    elif op == "1":
        n = [int(input(f"Num {i+1}/10: ")) for i in range(10)]
        print(f"Valores: {n}\nMaior: {max(n)}  Menor: {min(n)}")

    elif op == "2":
        n = [int(input(f"Num {i+1}/15: ")) for i in range(15)]
        print(f"Pares: {[x for x in n if x%2==0]}\nÍmpares: {[x for x in n if x%2!=0]}")

    elif op == "3":
        n = [int(input(f"Num {i+1}/8: ")) for i in range(8)]
        b = int(input("Buscar: "))
        print("Encontrado!" if b in n else "Não encontrado.")

    elif op == "4":
        n = [int(input(f"Num {i+1}/20: ")) for i in range(20)]
        print(f"Positivos: {sum(1 for x in n if x>0)}  Negativos: {sum(1 for x in n if x<0)}  Zeros: {sum(1 for x in n if x==0)}")

    elif op == "5":
        a = [int(input(f"L1 {i+1}/5: ")) for i in range(5)]
        b = [int(input(f"L2 {i+1}/5: ")) for i in range(5)]
        print(f"Comuns: {[x for x in a if x in b]}\nSó L1: {[x for x in a if x not in b]}\nSó L2: {[x for x in b if x not in a]}")

    elif op == "6":
        nomes = [input(f"Nome {i+1}: ") for i in range(5)]
        precos = [float(input(f"Preço {i+1}: ")) for i in range(5)]
        estoques = [int(input(f"Estoque {i+1}: ")) for i in range(5)]
        print("Estoque < 10:", [nomes[i] for i in range(5) if estoques[i] < 10])
        print("Mais caro:", nomes[precos.index(max(precos))], f"R${max(precos):.2f}")

    elif op == "7":
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i}x{j}={i*j}", end="  ")
            print()

    else:
        print("Opção inválida.")