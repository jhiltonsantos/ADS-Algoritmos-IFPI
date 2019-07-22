# entrada
valor_binario = int(input('Digite um numero binario de quatro digitos: '))

# processamento
numero1 = (valor_binario // 1000) * (2**3)
resto_num1 = valor_binario % 1000
numero2 = (resto_num1 // 100) * (2**2)
resto_num2 = resto_num1 % 100
numero3 = (resto_num2 // 10) * (2**1)
numero4 = (resto_num2 % 10) * (2**0)

valor_decimal = numero1 + numero2 + numero3 + numero4

# saida
print('O valor em decimal é: {}'.format(valor_decimal))

