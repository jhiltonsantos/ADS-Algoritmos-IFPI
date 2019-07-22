# entrada
custo_fabrica = float(input('Digite o valor do custo de fabrica do carro: '))

# processamento
custo_carro = custo_fabrica + (custo_fabrica * 0.28) + (custo_fabrica * 0.45)

# saida
print('O custo total do carro sera de: R${}'.format(custo_carro))
