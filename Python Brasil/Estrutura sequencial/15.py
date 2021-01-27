preco_hora = int(input('Digite o preço da sua hora trabalhada:'))
horas_trabalhadas = int(input('Digite quantas horas vc trabalhou no mês:'))

print('+ Salario Bruto = ', preco_hora*horas_trabalhadas)
print('- IR (11%) = ', (preco_hora*horas_trabalhadas)*0.11)
print('- INSS (8%) = ', (preco_hora*horas_trabalhadas)*0.08)
print('- SINDICATO (5%) = ', (preco_hora*horas_trabalhadas)*0.05)
print('= Salário Líquido = ', (preco_hora*horas_trabalhadas) - ((preco_hora*horas_trabalhadas)*0.11) - ((preco_hora*horas_trabalhadas)*0.08) - ((preco_hora*horas_trabalhadas)*0.05))
