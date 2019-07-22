#entrada
numero_a = float (input('Digite o A: '))
numero_b = float (input('Digite o B: '))
numero_c = float (input('Digite o C: '))

# processamento
expressao_r = (numero_a + numero_b) ** 2
expressao_s = (numero_b + numero_c) ** 2
expressao_d = (expressao_r + expressao_s) / 2

# saida
print('Resultado da expressao R: {} . Resultado da expressao S: {} . Resultado da expressao D: {}'\
    .format(expressao_r, expressao_s, expressao_d)) 