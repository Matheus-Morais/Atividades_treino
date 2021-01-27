metros_quadrados = int(input('Insira a area que irá ser pintada:'))

litros = metros_quadrados / 6

if (metros_quadrados % 6) > 0:
    latas = litros // 18
    galao = litros // 3.6

    latas = latas + 1
    galao = galao + 1

    aumento = litros * 1.1
    mistura_latas = aumento / 18
    resto = aumento % 3
    conversao = resto * mistura_latas
    mistura_galao = conversao // 3.6

    custo_latas = latas * 80
    custo_galao = galao * 25
    custo_mistura = (mistura_latas * 80 + mistura_galao * 25)

    print('A quantidade de latas necessárias é {} e o custo total é R${}:'.format(latas, custo_latas))
    print('A quantidade de galões necessários  é {} e o custo total é R${}:'.format(galao, custo_galao))
    print('A mistura seria de {} latas e {} galões, o custo total é R${}:'.format(mistura_latas, mistura_galao,
                                                                                custo_mistura))

else:

    latas = litros / 18
    custo = latas * 80
    print('A quantidade de latas necessária é {} e o custo total é {}:'.format(latas, custo))
