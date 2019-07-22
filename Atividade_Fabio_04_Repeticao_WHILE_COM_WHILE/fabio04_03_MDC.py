from tools import verifica_maior_menor

def main():
    valor_n1 = float(input('Primeiro Numero: '))
    valor_n2 = float(input('Segundo Numero: '))
    print('Maximo Divisor Comum: %.2f'%valor_mdc(valor_n1,valor_n2))


def valor_mdc(numero_1,numero_2):
    n1,n2 = verifica_maior_menor(numero_1,numero_2)
    while n2 != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    mdc = n1
    return mdc


if __name__ == '__main__':
    main()
