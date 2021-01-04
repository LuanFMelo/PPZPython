#Calculem a média dos dez números

n = 1
soma = 0

while n <= 10:
    x = int(input(f'{n} número: '))
    soma = soma + x
    n = n + 1
    
print(f'Média: {soma/10:.1f}')

#Contadores incremento constante
#Acumuladores variável

#Acumulador pode ser de produto

#fatorial de 10

#1 * 2 * 3 * ... * 9 * 10

############

k = 1 #Contador/incrementador
fat = 1 #Acumulador, elemento neutro

while k <= 10:
    fat = fat * k
    k = k + 1
print(f'fat(10) = {fat}')
