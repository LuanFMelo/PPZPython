salario_inicial=float(input('Digite o seu salário atual: '))
aumento=float(input('Qual a porcentagem de aumento? '))

aumento= (salario_inicial * aumento / 100)

print('O valor do aumento foi de: ', aumento)
print('O novo salário é: ', salario_inicial + aumento)
