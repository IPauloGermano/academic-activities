v1 = input('Digite algo: ')

print(type(v1))

try:
    tnum = float(v1)
    qd = tnum ** 2
    print('É numerico')
    print(qd)

except:
    print("Não é numérico, não é possível calcular o quadrado.")