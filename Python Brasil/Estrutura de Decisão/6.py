n1 = float(input('Insira um numero:'))
n2 = float(input('Insira um numero:'))
n3 = float(input('Insira um numero:'))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)