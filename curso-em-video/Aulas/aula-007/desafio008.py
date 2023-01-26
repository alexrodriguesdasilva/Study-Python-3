#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
n = float(input('Digite um valor em metro para descobrir seu valor em centímetros e milímetros: '))
cen = n * 100
mil = n * 1000

print(f'{n} metros em centimetros é {cen}\n{n} metros em milímetros é {mil}')