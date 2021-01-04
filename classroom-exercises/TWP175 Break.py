#Calcular o fatorial de um numero lido

k = 1 #Contador
fat= 1 #Fatorial
n = int(input('Digite o fatorial: '))

while k < n:
    fat = fat * k
print(f'fat({n}) = {fat}')
