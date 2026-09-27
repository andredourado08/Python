print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.')

import math
co = int(input('Digite o comprimento do cateto oposto: '))
ca = int(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {hip:.2f}')