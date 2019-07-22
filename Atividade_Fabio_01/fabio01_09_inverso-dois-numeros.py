# entrada
valor_numero = int(input('Digite o dois numeros: '))

# processamento
numeroA = valor_numero // 10
numeroB = valor_numero % 10

str_numeroA = str(numeroA)
str_numeroB = str(numeroB)

numero_inverso = str_numeroB + str_numeroA

# saida
print('Ordem inversa: {}'.format(numero_inverso))