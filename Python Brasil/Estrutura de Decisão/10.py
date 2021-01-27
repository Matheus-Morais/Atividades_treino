periodo = input('Insira o periodo que trabalha:')

if periodo == 'V' or periodo == 'v':
    print('Vespertino')
elif periodo == 'M' or periodo == 'm':
    print('Matutino')
elif periodo == 'N' or periodo == 'n':
    print('Noturno')
else:
    print('Periodo Inválido')