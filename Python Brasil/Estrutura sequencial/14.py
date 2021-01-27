peso = float(input('Insira o peso total:'))

if peso > 40:
    excesso = peso - 40
    multa = excesso * 4
    print('O peso total dos peixes é {}, teve um excesso de {} e terá de pagar a multa de R${}'. format(peso, excesso, multa))
else:
    print('O peso total dos peixes é ', peso)