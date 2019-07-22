def main():
    multiplo_n = int(input('Digite o multiplo: '))
    limite_interior = int(input('Digite o inicio do intervalo: '))
    limite_superior = int(input('Digite o limite: '))

    while limite_interior <= limite_superior:
        while limite_interior % multiplo_n == 0:
            print(limite_interior, end=' ')
            break
        limite_interior += 1


if __name__ == '__main__':
    main()