# entrada
valor_meses = int(input('Digite a quantidade de meses: '))

# processamento 
quant_ano = valor_meses // 12
quant_mes = valor_meses % 12

# saida
print('{} ano(s), {} mes(es).'.format(quant_ano, quant_mes))