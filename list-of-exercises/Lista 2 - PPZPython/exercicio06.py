hora_trabalhada= float(input('Quanto voce ganha por hora trabalhada ? '))
hora_mensal= float(input('Quantas horas voce trabalha por mes ? '))

salario_bruto = (hora_trabalhada * hora_mensal)
ir= ((11*salario_bruto)/100)
inss=((8*salario_bruto)/100)
sindicato=((5*salario_bruto)/100)
descontos=(ir+inss+sindicato)
salario_liquido=(salario_bruto-descontos)

print(f'+Salário Bruto:\t\t R$ {salario_bruto:.2f}')
print(f'-IR:\t\t\t R$ {ir:.2f}')
print(f'-INSS:\t\t\t R$ {inss:.2f}')
print(f'-Sindicato:\t\t R$ {sindicato:.2f}')
print(f'=Salário Líquido:\t R$ {salario_liquido:.2f}')

#\t => Igual um TAB
