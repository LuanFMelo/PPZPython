#Equilatero => Os 3 lados iguais - OK
#Isosceles =>  Os 2 lados iguais - OK
#Escaleno => Os 3 lados diferentes - OK

lado1= int(input('Digite o primeiro lado do triangulo: '))
lado2= int(input('Digite o segundo lado do triangulo: '))
lado3= int(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 == lado3:
    print('Esse é um triangulo Equilátero')

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado1 or lado2 == lado3 or lado3 == lado1 or lado3 == lado2:
    print('Esse e um triangulo Isosceles')
    
else:
    print('Esse é um triangulo Escaleno')

