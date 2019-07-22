# entrada
valor_segundos = int (input('Digite a quantidade em segundos: '))

# processamento
quant_horas = valor_segundos // 3600
resto_horas = valor_segundos % 3600
quant_minutos = resto_horas // 60
quant_segundos = resto_horas % 60


# saida
print ('{} Hora(s), {} Minuto(s), {} Segundo(s).'\
    .format(quant_horas,quant_minutos,quant_segundos))
