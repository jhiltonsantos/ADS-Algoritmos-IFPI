def main():
    valor = int(input())
    cont = 1
    sequencia_logica(valor,cont)


def sequencia_logica(valor,cont):
    i = 1
    j = 0
    k = 0
    quant = valor * 2

    while cont <= quant:
        x = 1
        while x <=2:
            if x == 1:
                j = i ** 2
                k = j * i
            
            elif x == 2:
                j += 1
                k += 1

            print('{} {} {}'.format(i,j,k))
            x += 1
        i += 1
        cont += 2 


if __name__ == '__main__':
    main()