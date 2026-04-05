n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

d1 = n1 %  3
d2 = n2 % 3
d3 = n3 % 3

if d1 > d2 and d1 > d3:
    if d2 >= d3:
        print(d1, d2, d3)
    else:
        print(d1, d3, d2)

elif d2 > d1 and d2 > d3:
    if d1 >= d3:
        print(d2, d1, d3)
    else:
        print(d2, d3, d1)

else:
    if d1 > d2:
        print(d3, d1, d2)
    else:
        print(d3, d2, d1)