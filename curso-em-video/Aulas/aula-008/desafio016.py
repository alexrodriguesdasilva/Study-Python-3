# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira
#
#Ex:
#Digite um numero: 6.127
#O número 6.127 tem a parte inteira 6
import math

n = float(input("digite um numero com ponto: "))
nInt = math.trunc(n)

print(f'A porção inteira do número {n} é: {nInt} ')
