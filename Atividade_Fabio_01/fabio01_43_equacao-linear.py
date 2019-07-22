# entrada
coef_a = float(input('Digite o valor do coeficiente A: '))
coef_b = float(input('Digite o valor do coeficiente B: '))
coef_c = float(input('Digite o valor do coeficiente C: '))
coef_d = float(input('Digite o valor do coeficiente D: '))
coef_e = float(input('Digite o valor do coeficiente E: '))
coef_f = float(input('Digite o valor do coeficiente F: '))

# processamento
valor_x = ((coef_c*coef_e) - (coef_b*coef_f)) / ((coef_a*coef_e) - (coef_b*coef_d))
valor_y = ((coef_a*coef_f) - (coef_c*coef_d)) / ((coef_a*coef_e) - (coef_b*coef_d))

# saida
print ('O valor de X é: {} . O valor de Y é: {}'.format(valor_x, valor_y))