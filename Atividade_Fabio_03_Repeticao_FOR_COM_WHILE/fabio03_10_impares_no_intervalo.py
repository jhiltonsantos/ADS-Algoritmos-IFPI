def main():
    limite_inferior = int(input('Digite o valor inicial: '))
    limite_superior = int(input('Digite o valor final: '))

    while limite_inferior <= limite_superior:
        while limite_inferior % 2 != 0:
            print(limite_inferior, end=' ')
            limite_inferior += 1
        limite_inferior += 1


if __name__ == '__main__':
    main()