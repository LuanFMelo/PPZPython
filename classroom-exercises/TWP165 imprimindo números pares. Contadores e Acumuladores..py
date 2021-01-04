#Contadores incremento constante X Acumuladores soma variável.

#Soma dez inteiros lidos

n = 1
soma = 0

while n <= 10:
    x = int(input(f'{n} número: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {soma}')
