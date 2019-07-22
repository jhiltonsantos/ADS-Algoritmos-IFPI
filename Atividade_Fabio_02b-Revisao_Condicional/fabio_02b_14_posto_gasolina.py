def main():
    litro_vendido = int(input('Numero de litro vendido: '))
    tipo_combustivel= input ('A-alcool||G-gasolina: ')

    if tipo_combustivel == 'A':
        if litro_vendido <= 20:
            desconto = 1.90 - (1.90 * 0.03)
            pagar = desconto * litro_vendido
            print('Valor pago em alcool: {}'.format(pagar))
        else:
            desconto = 1.90 - (1.90 * 0.05)
            pagar = desconto * litro_vendido
            print('Valor pago em alcool: {}'.format(pagar))
    
    elif tipo_combustivel == 'G':
        if litro_vendido <= 20:
            desconto = 2.5 - (2.5 * 0.04)
            pagar = desconto * litro_vendido
            print('Valor pago em gasolina: {}'.format(pagar))
        else:
            desconto = 2.5 - (2.5 * 0.06)
            pagar = desconto * litro_vendido
            print('Valor pago em gasolina: {}'.format(pagar))
    
    else:
        print('Valor invalido!')


if __name__ == '__main__':
    main()