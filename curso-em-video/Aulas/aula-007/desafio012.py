#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto

print('Olá, boa tarde, estamos com 5% de desconto em toda a loja')

compra = float(input('insire o valor de sua compra para calcular seu desconto: R$'))

desconto = compra *0.95

print(f'O valor da compra sem desconto é R${compra:.2f}\ncom desconto de 5% ficou R${desconto:.2f}\nEconomia de R${compra - desconto:.2f}')