print('faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preco=float(input('Qual o preço do produto ?'))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}')