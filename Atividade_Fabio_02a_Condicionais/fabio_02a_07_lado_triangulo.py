def main():
    lado_1 = int(input('Lado 1: '))
    lado_2 = int(input('Lado 2: '))
    lado_3 = int(input('Lado 3: '))
    
    if lado_1 == 0 or lado_2 == 0 or lado_3 == 0:
        print('Nao existe lado com tamanho 0')
    else:
        if (lado_1+lado_2) >= lado_3:
            if lado_1 == lado_2 and lado_2 == lado_3:
                print('Triangulo Equilatero')
            elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
                print('Triangulo Isosceles')
            elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
                print('Triangulo Escaleno')
        else:
            print('Nao é um triangulo')


if __name__ == '__main__':
    main()
    