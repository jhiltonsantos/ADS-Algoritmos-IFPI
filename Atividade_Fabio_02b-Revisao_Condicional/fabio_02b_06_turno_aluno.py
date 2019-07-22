def main():
    turno = input('Digite o turno: ')

    if turno=='m' or turno=='M':
        print('Bom Dia!')
    elif turno=='v' or turno=='V':
        print('Boa Tarde!')
    elif turno=='n' or turno=='N':
        print('Boa Noite!')
    else:
        print('Valor Invalido!')


if __name__ == '__main__':
    main()
