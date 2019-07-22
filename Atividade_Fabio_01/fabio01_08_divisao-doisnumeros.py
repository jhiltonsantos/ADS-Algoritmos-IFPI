# entrada
valor_numero = int(input('Digite o dois numeros: '))

# processamento
numero1 = valor_numero // 10
numero2 = valor_numero % 10

adicao = numero1 + numero2
subtracao = numero1 - numero2
divisao = adicao / subtracao
# saida
print('O resultado será: {}'.format(divisao))