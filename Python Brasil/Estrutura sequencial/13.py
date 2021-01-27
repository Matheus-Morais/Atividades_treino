altura = float(input('Insira a sua altura:'))
sexo = int(input('Homem = 1 / Mulher = 2 :'))

if sexo == 1:
    print('O seu peso ideal é:', (72.7 * altura) - 58)
else:
    print('O seu peso ideal é:', (62.1 * altura) - 44.7 )