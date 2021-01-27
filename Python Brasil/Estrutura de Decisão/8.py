n1 = float(input('Insira o valor do produto:'))
n2 = float(input('Insira o valor do produto:'))
n3 = float(input('Insira o valor do produto:'))

if n1 < n2 and n1 < n3:
    print('R$',n1)
elif n2 < n1 and n2 < n3:
    print('R$',n2)
else:
    print('R$',n3)