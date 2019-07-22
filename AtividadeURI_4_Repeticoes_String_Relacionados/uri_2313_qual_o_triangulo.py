    def main():
        a, b, c = map(int, input().split())

        if (abs(b-c)<a and b+c>a) and\
            (abs(a-c)<b and a+c>b) and\
                (abs(a-b)<c and a+b>c):
            if a==b and a==c and b==c:
                print('Valido-Equilatero')
            elif (a==b and a!=c) or (b==c and b!=a) or\
                (c==a and c!=b):
                print('Valido-Isoceles')
            elif (a!=b and a!=c) and b!=c:
                print('Valido-Escaleno')

            if (a**2 == ((b**2)+(c**2))) or\
                (b**2 == ((a**2)+(c**2))) or\
                    (c**2 == ((a**2)+(b**2))):
                print('Retangulo: S')
            else:
                print('Retangulo: N')

        else:
            print('Invalido')


    main() 