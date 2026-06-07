def calcular_perimetro(largura, comprimento):
    return (2 * largura) + (2 * comprimento)


largura = float(input("Informe a largura: "))
comprimento = float(input("Informe o comprimento: "))

perimetro = calcular_perimetro(largura, comprimento)

print("Perímetro do retângulo:", perimetro)