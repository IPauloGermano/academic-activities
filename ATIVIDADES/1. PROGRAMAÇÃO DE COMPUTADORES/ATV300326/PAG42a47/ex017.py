age = int(input('Qual sua idade? '))

if age < 18:
    print('Menor de idade')
elif age < 60 :
    print('Adulto')
else:
    print('Idoso')