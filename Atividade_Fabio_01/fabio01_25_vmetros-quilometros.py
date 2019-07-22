# entrada
valor_metro = float(input('Quantidade em metros:'))

# processamento
quant_km = valor_metro // 1000
quant_metros = valor_metro % 1000

# saida

print('Resultado: {} quilometros {} metros'.format(quant_km,quant_metros))
 