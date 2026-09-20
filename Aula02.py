print('Tipos Primitivos em Python')

print('Numeros Inteiros')
n1 = int(input('Numero 01: '))
n2 = int(input('Numero 02: '))
soma = n1 + n2
print(f'A soma dos numeros {n1} e {n2} é igual a {soma}') 

print('Numeros Reais')
n3= float(input('Numero 03: '))
n4= float(input('Numero 04: '))
soma = n3 + n4
print(f'A soma dos numeros {n3} e {n4} é igual a {soma}') 

print('numeros booleanos')
v1 = bool(input('Valor 01: '))
v2 = bool(input('Valor 02: '))
print(f'O valor {v1} e {v2} é igual a {v1 and v2}')

print('Strings')
men=str(input('Digite uma mensagem: '))
print(f'A mensagem digitada foi: {men}')

print('Desafio04- Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.')

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'É numérico? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')