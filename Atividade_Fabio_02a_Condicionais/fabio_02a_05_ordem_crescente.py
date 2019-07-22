def main():
    numero_1 = int(input('Primeiro numero: '))
    numero_2 = int(input('Segundo numero: '))
    numero_3 = int(input('Terceiro numero: '))

    if numero_2 < numero_1 > numero_3 and numero_2 > numero_3:
        print('{} {} {}'.format(numero_1, numero_2, numero_3))

    elif numero_2 < numero_1 > numero_3 and numero_3 > numero_2:
        print('{} {} {}'.format(numero_1, numero_3, numero_2))

    elif numero_1 < numero_2 > numero_3 and numero_1 > numero_3:
        print('{} {} {}'.format(numero_2, numero_1, numero_3))
    
    elif numero_3 < numero_2 > numero_1 and numero_3 > numero_1:
        print('{} {} {}'.format(numero_2, numero_3, numero_1))
    
    elif numero_1 < numero_3 > numero_2 and numero_1 > numero_2:
        print('{} {} {}'.format(numero_3, numero_1, numero_2))

    elif numero_2 < numero_3 > numero_1 and numero_2 > numero_1:
        print('{} {} {}'.format(numero_3, numero_2, numero_1))
    

if __name__ == '__main__':
    main()