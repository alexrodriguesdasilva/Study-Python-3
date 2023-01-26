#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta, pinta uma área de 2m²

print('Calculadora de pintura\nsabendo que cada litro de tita, pinta uma area de 2m²\ninforme:')
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

metroQuadrado = largura * altura

print(f'sua parede tem {metroQuadrado}m²\nVocê precisara de {metroQuadrado/2}L de tinta')