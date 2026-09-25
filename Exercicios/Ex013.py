print('Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.')

salario=float(input('Qual o salário do funcionário ?'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'O funcionário que ganhava R${salario:.2f}, com aumento de 15% vai passar a ganhar R${novo_salario:.2f}')