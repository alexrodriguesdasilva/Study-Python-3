# Enviar um email com detalhes da compra online(Maximo 3 tentativas)
# para compras confirmadas

compra_confirmada = True #False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes envado para o seu email')
        break
else:
    print('Falha na compra')