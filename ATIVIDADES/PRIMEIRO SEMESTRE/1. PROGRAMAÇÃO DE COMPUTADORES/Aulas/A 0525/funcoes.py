def soma():
    so = 0
    for x in range(2):
        n = int(input('Digite um num: '))
        so += n
    print(so)
    return so


def aoQuadrado(): # criei uma func
    q = 0 # variavel q pra receber o valor de n ao quadrado
    n = int(input('Digite um num: ')) # input do user
    q = n ** 2 # atribuiçao de n**2 a q
    print(q) # printa valo de n**2
    return q # retorna valor de q a funçao

def create():
    

     return


def read():
    p = input('Digite uma frase: ')
    print(f'Em {p} tem {len(p)} letras')
    return p

# def update():


#     return

# def delete():

#     return

#########################################

def escrever():
    arquivo = open('dados.txt', 'w')
    x = input('Digita: ')
    arquivo.write(x)
    arquivo.close()
    return arquivo