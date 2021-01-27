nota1 = float(input('Insira a nota:'))
nota2 = float(input('Insira a segunda nota:'))

media = (nota1+nota2)/2

if media == 10:
    print('Aprovado com Distinção')
if media < 7:
    print('Reprovado')
else:
    print('Aprovado')

