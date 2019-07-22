# entrada
minutos = int(input('Digite o valor em minutos: '))

# processamento
valor_horas = minutos // 60
valor_minutos = minutos % 60

# saida
print ('{} hora(s), {} minuto(s).'.format(valor_horas,valor_minutos))


