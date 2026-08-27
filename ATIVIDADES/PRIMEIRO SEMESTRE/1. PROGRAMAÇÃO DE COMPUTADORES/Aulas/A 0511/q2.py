l = []

for i in range(7):
    n = int(input("Digite um número inteiro: "))
    l.append(n)

print("Valores em ordem inversa:")
for i in range(len(l)-1, -1, -1):
    print(l[i])