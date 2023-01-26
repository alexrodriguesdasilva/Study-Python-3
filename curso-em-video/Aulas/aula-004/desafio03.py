from doctest import DocFileSuite


#Crie um script Python que leia dois 
#números e tente mostrar a soma entre eles 

print('Vamos somar dois numeros?')
primeiro_numero=input('Digite o primeiro numero: ')
segundo_numero=input('Digite o segundo numero: ')

resultado=int(primeiro_numero)+int(segundo_numero)

print('A soma de', primeiro_numero,'+', segundo_numero,'=', resultado)