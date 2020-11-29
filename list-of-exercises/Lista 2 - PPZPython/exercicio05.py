# 5. Faça um Programa que leia três números e mostre o maior e o menor deles.



a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

if a > b and a > c:
    valor_maior=a
else:
    if b > a and b > c:
        valor_maior=b
    else:
        if c > a and c > b:
            valor_maior=c
        else:
            if a < b and a < c:
                valor_menor=a
            else:
                if b < a and b < c:
                    valor_menor=b
                else:
                    if c < a and c < b:
                        valor_menor=c
                    else:
                        print('Todos os valores são iguais!')

print('O maior valor é: ', valor_maior)
print('O menor valor é: ', valor_menor)

                        


