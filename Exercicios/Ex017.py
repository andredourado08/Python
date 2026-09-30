print('um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')

import random
a1= input('Digite o nome do primeiro aluno: ')
a2= input('Digite o nome do segundo aluno: ')
a3= input('Digite o nome do terceiro aluno: ')
a4= input('Digite o nome do quarto aluno: ')
alunos= [a1, a2, a3, a4]
escolhido= random.choice(alunos)
print(f'O aluno escolhido foi: {escolhido}')