import random, math

# Define o intervalo do jogo: o número secreto estará entre 0 e 1000
n = 1000
numero = random.randint(0, n)  # Sorteia o número que o jogador deve adivinhar

# Pede ao jogador que escolha o modo de jogo
modo = input("Modo — 1: sem dicas  2: com dicas\nOpção: ")
tentativas = 0  # Contador de tentativas

if modo not in ("1", "2"):
    print("Opção inválida")
else:
    # Loop infinito — só encerra quando o jogador acertar (break)
    while True:
        chute = int(input("Seu chute: "))
        tentativas += 1  # Incrementa o contador a cada palpite

        if chute == numero:
            # Monta a referência de complexidade conforme o modo escolhido:
            # Modo 1 → busca linear: pior caso percorre todos os n elementos → O(n)
            # Modo 2 → busca binária: cada tentativa elimina metade → O(log₂ n)
            ref = f"pior caso ~{n}" if modo == "1" else f"≈ log₂({n}) = {math.log2(n):.2f}"
            print(f"✔️ Acertou em {tentativas} tentativas ({ref})")
            break  # Encerra o loop ao acertar

        elif modo == "1":
            # Sem dicas: comportamento de busca linear — jogador não tem como
            # descartar possibilidades, então pode precisar de até n tentativas
            print("❌ Errado")

        elif chute < numero:
            # Dica "muito baixo": jogador sabe que pode descartar tudo abaixo do chute
            # Isso é a essência da busca binária — eliminar metade do espaço de busca
            print("📉 Muito baixo")

        else:
            # Dica "muito alto": descarta tudo acima do chute
            print("📈 Muito alto")