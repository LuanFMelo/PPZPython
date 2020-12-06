# 5. Faça um Programa que leia três números e mostre o maior e o menor deles.

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

if a > b and a > c:
    valor_maior=a
    if b > c:
        valor_menor=c
    else:
        valor_menor=b
else:
    if b > a and b > c:
        valor_maior=b
        if a > c:
            valor_menor=c
        else:
            valor_menor=a
    else:
        valor_maior=c
        if b < a:
            valor_menor=b
        else:
            valor_menor=a

print('O maior valor é: ', valor_maior)
print('O menor valor é: ', valor_menor)

