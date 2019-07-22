def main():
    valor = int(input())

    print('N[0] = %d' % valor)
    i = 1
    while i < 10:
        valor = valor*2
        print('N[%d] = %d' % (i, valor))
        i += 1

main()