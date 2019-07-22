def main():
    limite_interior = int(input('Digite o inicio do intervalo: '))
    limite_superior = int(input('Digite o limite: '))

    while limite_interior <= limite_superior:
       
        while limite_interior % 2 == 0:
            print(limite_interior, end=' ')
            break
        limite_interior += 1


if __name__ == '__main__':
    main()