n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2 
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 * n2
r = n1 % n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e pontencia {}'.format(di, e))
print('A subtração é {} e o resto é {}'.format(sb, r))