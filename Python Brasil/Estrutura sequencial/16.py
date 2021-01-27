metros_quadrados = int(input('Insira a area que irá ser pintada:'))

litros = metros_quadrados / 3

if (metros_quadrados % 3) >= 0:
    latas = litros // 18
    latas = latas + 1
    custo = latas * 80
    print('A quantidade de latas necessária é {} e o custo total é {}:'.format(latas, custo))
else:
    latas = litros / 18
    custo = latas * 80
    print('A quantidade de latas necessária é {} e o custo total é {}:'.format(latas, custo))