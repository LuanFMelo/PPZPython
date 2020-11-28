peso= float(input('Digite o peso dos peixes: '))

if peso>50:
    excesso=(peso - 50)
    multa=(excesso*4)
    print('O excesso de peixes é: ', excesso )    
    print('O valor da multa é de: ', multa )

elif peso==50:

    print('O valor está no limite, não há excesso nem multas')

else:
    excesso=0
    multa=(excesso*4)
    print('O excesso de peixes é: ', excesso )
    print('O valor da multa é de: ', multa )
