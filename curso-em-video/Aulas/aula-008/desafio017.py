# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triangulo retangulo, calcule e mostre
# o comprimento da hipotenusa

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.sqrt(co ** 2 + ca ** 2)

print(f'O valor do comprimento da hipotenusa é: {hi:.2f}')