# entrada
numero = int(input('Digite um numero de tres digitos: '))


# processamento
num1 = numero // 100
resto1 = numero % 100
num2 = resto1 // 10
num3 = resto1 % 10

primeiros = num1 + num2
ultimos = num2 + num3

# saida
print('A soma dos dois primeros: {}. A soma dos dois ultimos: {}'.format(primeiros,ultimos))