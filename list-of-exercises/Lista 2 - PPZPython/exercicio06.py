hora_trabalhada= float(input('Quanto voce ganha por hora trabalhada ? '))
hora_mensal= float(input('Quantas horas voce trabalha por mes ? '))

salario_bruto = (hora_trabalhada * hora_mensal)

print('+','Salário Bruto: ','R$',salario_bruto)

ir= ((11*salario_bruto)/100)

print('-','IR: ','R$',ir)

inss=((8*salario_bruto)/100)

print('-','INSS: ','R$', inss)

sindicato=((5*salario_bruto)/100)

print('-','Sindicato: ','R$', sindicato)

descontos=(ir+inss+sindicato)

salario_liquido=(salario_bruto-descontos)

print('=','Salário Líquido: ','R$', salario_liquido)
