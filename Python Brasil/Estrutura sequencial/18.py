'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
 calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

tamanho = float(input('Insira o tamanho do arquivo em MB:'))
velocidade = float(input('Insira a velocidade da sua internet em Mbps:'))

tempo = (tamanho / velocidade)/60

tempo_arredondado = round(tempo, 1)


print('O tempo aproxiamdo que será gasto no download é {} minutos '.format(tempo_arredondado) )