#4. Receba uma frase e substitua todas as ocorrências de uma palavra específica
#por outra.

p = input('Digite uma frase: ').lower()
s = 'python'

if s in p:
    p = p.replace('python','java')
       
print(p)
