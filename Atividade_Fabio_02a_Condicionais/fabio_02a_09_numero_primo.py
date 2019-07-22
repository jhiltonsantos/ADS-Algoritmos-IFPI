def main():
    numero = int(input('Numero: '))

    if 0 < numero < 100:
        if numero != 0 and numero !=1:
            if numero == 2:
                print('1numero primo')
            elif numero >= 3:
                for i in range(2,numero):
                    if numero % i == 0:
                        print('numero nao primo')               
        else:
            print('4numero nao primo')


if __name__ == '__main__':
    main()