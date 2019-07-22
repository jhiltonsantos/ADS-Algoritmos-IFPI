# entrada
valor_horas = int (input('Digite a quantidade de horas: '))

# processamento
quant_semana = valor_horas // 168
resto_semana = valor_horas % 168
quant_dia = resto_semana // 24
quant_hora = resto_semana % 24

# saida
print('{} semana(s), {} dia(s), {} hora(s).'\
    .format(quant_semana,quant_dia,quant_hora))

