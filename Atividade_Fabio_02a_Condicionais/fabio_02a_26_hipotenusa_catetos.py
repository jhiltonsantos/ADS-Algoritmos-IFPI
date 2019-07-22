def main():
    lado_1 = int(input('Lado 1: '))
    lado_2 = int(input('Lado 2: '))
    lado_3 = int(input('Lado 3: '))

    if lado_1 > lado_2 and lado_1 > lado_3:
        print('Hipotenusa: {}. Catetos: {} e {}'\
            .format(lado_1,lado_2,lado_3))
    elif lado_2 > lado_1 and lado_2 > lado_3:
        print('Hipotenusa: {}. Catetos: {} e {}'\
            .format(lado_2,lado_1,lado_3))
    elif lado_3 > lado_1 and lado_3 > lado_2:
        print('Hipotenusa: {}. Catetos: {} e {}'\
            .format(lado_3,lado_1,lado_2))


if __name__ == '__main__':
    main()