'''
Fazendo regra de tres
1 dia = 1440 minutos = 144 cigarros
'''
cigarros=float(input('Quantos cigarros voce fuma por dia? '))
anos=float(input('Quantos anos voce fumou?'))

total_cigarros = anos * 365 * cigarros
dias = total_cigarros /144

print(f'Voce perdeu {dias:.1f} dias')
