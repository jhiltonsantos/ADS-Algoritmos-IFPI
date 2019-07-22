def main():
    numero_1 = int(input('Primeiro numero: '))
    numero_2 = int(input('Segundo numero: '))

    if (numero_1 > numero_2):
        print('Primeiro numero é o maior numero. E o segundo é o menor.')
    else:
        print('Segundo numero é o maior numero. E o primeiro é o menor.')


if __name__ == '__main__':
    main()