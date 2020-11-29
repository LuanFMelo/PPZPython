# 4.Faça um Programa que leia três números e mostre o maior deles.


a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

if a > b and a > c:
    print('O primeiro número é maior deles:', a)
else:
    if b > a and b > c:
        print('O segundo número é o maior deles: ', b)
    else:
        if c > a and c > b:
            print('O terceiro número é o maior deles:', c)
        else:
            print('Todos os números são iguais')
