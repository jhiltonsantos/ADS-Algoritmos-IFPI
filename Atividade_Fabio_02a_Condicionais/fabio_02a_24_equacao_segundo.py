def main():
    valor_a = float(input('Valor de A: '))
    valor_b = float(input('Valor de B: '))
    valor_c = float(input('Valor de C: '))

    if valor_a != 0:
        delta = (valor_b**2) - (4*valor_a*valor_c)
        if delta == 0:
            raiz_positivo = (-(valor_b) + (delta**(1/2))) / (2*valor_a)
            print('Valor de delta: {:.2f}'.format(delta))
            print('Valor das raizes sao iguais: {:.2f}'.format(raiz_positivo))
        elif delta > 0:
            raiz_positivo = (-(valor_b) + (delta**(1/2))) / (2*valor_a)
            raiz_negativo = (-(valor_b) - (delta**(1/2))) / (2*valor_a)
            print('Valor de delta: {:.2f}'.format(delta))
            print('Raiz Positiva: {:.2f}. Raiz Negativa: {:.2f}.'\
                .format(raiz_positivo,raiz_negativo))
        else:
            print('Valor de delta: {:.2f}'.format(delta))
            print('Delta invalido')
    else:
        print('Valor de A invalido!!!')


if __name__ == '__main__':
    main()