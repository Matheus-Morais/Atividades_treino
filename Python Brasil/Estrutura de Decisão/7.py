n1 = float(input('Insira um numero:'))
n2 = float(input('Insira um numero:'))
n3 = float(input('Insira um numero:'))

if n1 > n2 > n3 and n1 > n3:
    print('maior:',n1)
    print('menor:',n3)
elif n1 > n2 and n1 > n3 > n2:
    print('maior:', n1)
    print('menor:', n2)
elif n2 > n1 > n3 and n2 > n3:
    print('maior:', n2)
    print('menor:', n3)
elif n2 > n1 and n2 > n3 > n1:
    print('maior:', n2)
    print('menor:', n1)
elif n3 > n1 > n2 and n3 > n2:
    print('maior:', n3)
    print('menor:', n2)
else:
    print('maior:', n3)
    print('menor:', n1)