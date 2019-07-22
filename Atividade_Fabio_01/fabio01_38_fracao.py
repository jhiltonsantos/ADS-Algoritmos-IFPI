#entrada

fracao1_numerador = int (input('Digite o numerador da primeira fracao: '))
fracao1_denominador = int (input('Digite o denominador da primeira fracao: '))
fracao2_numerador = int (input('Digite o numerador da segunda fracao: '))
fracao2_denominador = int (input('Digite o denominador da segunda fracao: '))

# processamento
denominador_novo = (fracao1_denominador * fracao2_denominador)

numerador_novo = ((denominador_novo // fracao1_denominador) * fracao1_numerador) + \
	((denominador_novo // fracao2_denominador) * fracao2_numerador)

# saida
print('{}/{}'.format(numerador_novo, denominador_novo))
