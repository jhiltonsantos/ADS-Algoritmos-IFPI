# entrada
valor_numero = int(input('Digite o tres numeros: '))

# processamento
numero1 = valor_numero //100
resto_num1 = valor_numero % 100
numero2 = resto_num1 // 10
numero3 = resto_num1 % 10

numero_inverso = (str(numero3)) + (str(numero2)) + (str(numero1))

# saida
print ('Inverso: {} .'.format(numero_inverso))