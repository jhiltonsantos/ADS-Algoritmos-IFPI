# entrada
print('Informe sua idade para o calculo dela em dias!!!')
idade_ano = int (input('Digite quantos ano(s): '))
idade_mes = int (input('Digite quantos mes(es): '))
idade_dias = int (input('Digite quantos dia(s): '))

# processamento
calc_dias = (idade_ano * 360) + (idade_mes * 30) + (idade_dias)

# saida
print('A sua idade é de: {} dia(s).'.format(calc_dias))