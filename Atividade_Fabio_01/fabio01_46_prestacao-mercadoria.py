# entrada
valor_mercadoria = int(input('Digite o valor da mercadoria: '))

# processamento
#divide o valor da mercadoria em tres inteiros
divisao_inteira = valor_mercadoria // 3
#soma o valor inteiro mais o resto
valor_entrada = (divisao_inteira) + valor_mercadoria % 3
#divide as parecelas em valores iguais
parcelas_valor = (valor_mercadoria - valor_entrada) / 2

#saida
print('O valor da entrada será de: R${}, e as parecelas de : R${}'\
	.format(valor_entrada, parcelas_valor))
