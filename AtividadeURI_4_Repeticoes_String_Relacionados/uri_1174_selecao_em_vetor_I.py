def main():
    i = 0
    while i < 100:
        valor = float(input())
        if valor <= 10:
            print('A[%d] = %.1f' % (i, valor))
        i += 1 


main()