#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Digite um numero: '))
su = n + 1
an = n - 1

print('O numero digitado é: {} \n\nSeu sucesso é: {} \nE seu antecessor é: {}'.format(n, su, an))