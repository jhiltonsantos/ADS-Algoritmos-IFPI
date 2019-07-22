# entrada
valor_minutos = int(input('Digite o valor em minutos: '))

# processamento
quant_dia = valor_minutos // 1440
resto_dia = valor_minutos % 1440
quant_hora = resto_dia // 60
quant_minuto = resto_dia % 60

# saida
print('{} dia(s), {} hora(s), {} minuto(s)'\
    .format(quant_dia, quant_hora, quant_minuto))
  