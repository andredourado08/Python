print('Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')

import math 
angulo= float(input('Digite o valor do ângulo: '))
print(f'O ângulo de {angulo} tem o seno de {math.sin(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {math.cos(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a tangente de {math.tan(math.radians(angulo)):.2f}')