#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu salário, com 15% de aumento.

print('Calculadora de 15% de aumento salarial')

salario = float(input('Insira seu salário atual: R$'))

print(f'Seu salario atual é de R${salario:.2f}\ncom aumento de 15% foi para R${salario*1.15:.2f}')