mercadoria=float(input('Digite o valor da mercadoria: '))
desconto=float(input('Qual a porcentagem de desconto? '))

desconto= (mercadoria * desconto / 100)

print('O valor do desconto foi de: ', desconto)
print('O valor da mercadoria com desconto é: ', mercadoria - desconto)
