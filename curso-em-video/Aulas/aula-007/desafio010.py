#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27

print('Essa calculadora converte o Reais para Dólares')
print('US$1.00 = R$3.27')
dinheiro = float(input('Insira o valor que gostaria de converter: R$'))

print(f'O valor de R${dinheiro} em Dólares é = US${dinheiro * 3.27}')