n1 = input('Digite um número: ')


try:
    num = int(n1)
    
    if num > 10:
        print("Alto")
    else:
        print("Baixo")

except:
    print("Entrada inválida")