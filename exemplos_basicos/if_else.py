velocidade = int(input("Digite a velocidade que o veiculo está em movimento na via: "))

if velocidade > 110:
    print('Acima da Velocidade Permitida')
    print('Favor Reduzir a sua velocidade')
elif velocidade < 60:
    print('Favor dirigir acima de 80Km/h')
else:
    print('Velocidade OK')