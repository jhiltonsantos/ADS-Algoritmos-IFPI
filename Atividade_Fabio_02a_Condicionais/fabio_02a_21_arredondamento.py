def main():
    numero = float(input('Digite o numero: '))

    if numero % 1 >= 0.5:
        numero = (numero + 0.5) // 1
        print('Numero arredondado: {}'.format(numero))
    else:
        numero = ((numero - 0.5) // 1) + 1
        print('Numero arredondado: {}'.format(numero))


if __name__ == '__main__':
    main()