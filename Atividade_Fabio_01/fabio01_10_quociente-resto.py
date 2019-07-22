# entrada
valor_numero = int(input('Digite o dois numeros: '))

# processamento
numero1 = valor_numero // 10
numero2 = valor_numero % 10

quociente = numero1 // numero2
resto = numero1 - (quociente*numero2)

# saida
print('O quociente da divisão dos dois numeros é: {} e \
       o resto {}'.format(quociente,resto))
