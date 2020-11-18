velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 110:
    print(f'Você foi multado !')
    multa = ((velocidade - 110) * 5)
    print (f'Multa R$ {multa:.2f}')
else:
    print('Siga em frente')
