# entrada
idade_dias = int (input('Informe sua idade em dias: '))

# processamento
calc_ano = idade_dias // 360
resto_ano = idade_dias % 360
calc_mes = resto_ano // 30
calc_dias = resto_ano % 30

# saida
print('A sua idade é de: {} ano(s), {} mes(es), \
	{} dia(s).'.format(calc_ano, calc_mes, calc_dias))