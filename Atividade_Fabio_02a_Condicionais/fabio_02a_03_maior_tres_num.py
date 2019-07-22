def main():
    numero_1 = int(input('Numero 1: '))
    numero_2 = int(input('Numero 2: '))
    numero_3 = int(input('Numero 3: '))

    if (numero_1 > numero_2) and (numero_1 > numero_3):
        print('Numero 1 é o maior!!!')
    elif (numero_2 > numero_1) and (numero_2 > numero_3):
        print('Numero 2 é o maior!!!')
    elif (numero_3 > numero_1) and (numero_3 > numero_2):
        print('Numero 3 é o maior!!!')

    
if __name__ == '__main__':
    main()