def main():
    numero = int(input('Digite numero: '))

    str_milhar = str(numero // 1000)
    resto_milhar = numero % 1000
    str_centena = str(resto_milhar // 100)
    resto_centena = resto_milhar % 100
    str_dezena = str(resto_centena // 10)
    str_unidade = str(resto_centena % 10)

    num_1 = int(str_dezena + str_unidade)
    num_2 = int(str_milhar + str_centena)
    num_3 = num_1 + num_2

    if numero == (num_3 ** 2):
        print('Valor exato')
    else:
        print('Valor errado')


if __name__ == '__main__':
    main()
