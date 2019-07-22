def main():
    angulo_1 = int(input('Angulo 1: '))
    angulo_2 = int(input('Angulo 2: '))
    angulo_3 = int(input('Angulo 3: '))
    
    if angulo_1 == 0 or angulo_2 == 0 or angulo_3 == 0:
        print('Nao existe lado com angulo 0°')
    else:
        if (angulo_1+angulo_2+angulo_3) == 180:
            if angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
                print('Triangulo Acutangulo')
            elif angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
                print('Triangulo Retangulo')
            elif angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90:
                print('Triangulo Obtusangulo')
        else:
            print('Nao é um triangulo')


if __name__ == '__main__':
    main()