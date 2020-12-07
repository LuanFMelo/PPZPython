# 4.Faça um Programa que leia três números e mostre o maior deles.


a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

if a >= b and a >= c:
    print(f'Maior: {a}')
elif b >= c:
    print(f'Maior: {b}')
else:
    print (f'Maior: {c}')
