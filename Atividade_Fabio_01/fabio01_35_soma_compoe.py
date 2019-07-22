# entrada
valor_num = int(input('Digite o valor do numero de quatro digitos: '))

# processamento
num1 = valor_num // 1000
resto_num1 = valor_num % 1000
num2 = resto_num1 // 100
resto_num2 = resto_num1 % 100
num3 = resto_num2 // 10
num4 = resto_num2 % 10

soma = num1 + num2 + num3 + num4

# saida
print('A soma dos quatro digitos é: {}'.format(soma))
