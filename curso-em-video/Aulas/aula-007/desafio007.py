# Desenvolva um programa que leia as duas notas de um aluno, Calcule e mostre a sua média.

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))

media = (n1 + n2)/2
print('Sua primeira nota foi: {}\nSua segunda nota foi: {}\n\nMedia final: {}'.format(n1, n2, media))