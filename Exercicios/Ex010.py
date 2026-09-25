print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.' \
'considere US$1,00 = R$3,27')

real= float(input('Quanto dinheiro você tem na carteira ? '))
conversor= real / 3.27
print(f'Com R${real:.2f} você pode comprar US${conversor:.2f}')