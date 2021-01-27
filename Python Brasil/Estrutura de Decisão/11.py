'''s Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''

salario: int = int(input('Insira seu salario:'))

if salario <= 280:
    aumento = 20
    reajuste = 0.2 * salario
    novo_salario = reajuste + salario
    print('Salario anterior:', salario)
    print('Percentual de aumento:', aumento)
    print('Reajuste:', reajuste)
    print('Novo salario:', novo_salario)
elif 280 < salario < 700:
    aumento = 15
    reajuste = 0.15 * salario
    novo_salario = reajuste + salario
    print('Salario anterior:', salario)
    print('Percentual de aumento:', aumento)
    print('Reajuste:', reajuste)
    print('Novo salario:', novo_salario)
elif 700 < salario < 1500:
    aumento = 10
    reajuste = 0.1 * salario
    novo_salario = reajuste + salario
    print('Salario anterior:', salario)
    print('Percentual de aumento:', aumento)
    print('Reajuste:', reajuste)
    print('Novo salario:', novo_salario)
else:
    aumento = 5
    reajuste = 0.05 * salario
    novo_salario = reajuste + salario
    print('Salario anterior:', salario)
    print('Percentual de aumento:', aumento)
    print('Reajuste:', reajuste)
    print('Novo salario:', novo_salario)