def main():
    valor_m = int(input('N1: '))
    valor_n = int(input('N2: '))

    cont = 0
    soma = 0
    while valor_m <= valor_n:
        soma = soma + valor_m
        valor_m += 1
        cont += 1
    media = soma / cont
    print('A soma é: ',soma)
    print('Media: ',media)


if __name__ == '__main__':
    main()
    