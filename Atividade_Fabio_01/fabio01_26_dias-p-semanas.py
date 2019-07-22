# entrada
valor_dia = int (input('Digite a quantidade de dias: '))

# processamento
quant_semanas = valor_dia // 7
quant_dias = valor_dia % 7


# saida
print ('{} semanas e {} dias.'.format(quant_semanas, quant_dias) )

