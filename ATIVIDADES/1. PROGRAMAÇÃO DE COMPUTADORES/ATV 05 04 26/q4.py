'''
> Em uma pesquisa de cinema, 15 espectadores avaliaram um filme com as seguintes opções:
>
> * 3 – Ótimo
> * 2 – Bom
> * 1 – Regular
>
> Escreva um programa que leia as respostas e informe a quantidade de avaliações de cada opção.
'''
oti = 0
bom = 0
reg = 0


for t in range(1, 16):
    r = int(input("Digite sua opinião (3-Ótimo, 2-Bom, 1-Regular): "))

    if r == 3:
        oti += 1
    elif r == 2:
        bom += 1
    elif r == 1:
        reg += 1
    
print("Quantidade de pessoas que responderam Ótimo:", oti)
print("Quantidade de pessoas que responderam Bom:", bom)
print("Quantidade de pessoas que responderam Regular:", reg)