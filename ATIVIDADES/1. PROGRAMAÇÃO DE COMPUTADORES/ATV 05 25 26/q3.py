def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print("Média:", media)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")