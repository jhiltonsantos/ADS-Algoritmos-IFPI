# entrada
valor_numero = int(input('Digite um numero de tres digitos: '))

# processamento
num1 = valor_numero // 100
resto_num1 = valor_numero % 100
num2 = resto_num1 // 10
num3 = resto_num1 % 10

inverso = int(str(num3) + str(num2) + str(num1))
result_soma = valor_numero + inverso

# saida
print('A soma dos numeros sera de: {}'.format(result_soma))
