a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

# descobrir o menor
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

# descobrir o maior
if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

meio = a + b + c - menor - maior

print(menor, meio, maior)