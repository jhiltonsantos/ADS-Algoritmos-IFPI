def main():
    preco_1 = float(input('Produto um: '))
    preco_2 = float(input('Produto dois: '))
    preco_3 = float(input('Produto tres: '))

    if preco_1 < preco_2 and preco_1 < preco_3:
        print('Primeiro produto deve ser comprado.')
    elif preco_2 < preco_1 and preco_2 < preco_3:
        print('Segundo produto deve ser comprado.')
    else:
        print('Terceiro produto deve ser comprado')


if __name__ == '__main__':
    main()
