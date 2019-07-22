# entrada
ano_fumante = int (input('Numero de anos como fumante: '))
quantidade_cigarro = int (input('Numero de cigarros por dia: '))
preco_carteira = float (input('Qual o preco da carteira de cigarros? '))

# processamento
valor_gasto = (ano_fumante*360) * (quantidade_cigarro*(preco_carteira/20))

# saida
print('A quantidade de dinheiro gasta em cigarros sera de: R${}'.format(valor_gasto))
