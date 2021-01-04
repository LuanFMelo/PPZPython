##########

#Repetições bem definidas, e se, eu não soubesse quando terminar ?

#Ex: Quero somar até a pessoa digitar um zero


soma = 0

while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    soma = soma + x
print(f'Soma: {soma}')
