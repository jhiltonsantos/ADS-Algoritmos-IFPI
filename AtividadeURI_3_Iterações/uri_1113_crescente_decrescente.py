def main():
    valor_x = 1
    valor_y = 0

    while valor_x != valor_y:
        valor_x, valor_y = map(int, input().split())
        if valor_x == valor_y:
            break
        elif valor_x > valor_y:
            print('Decrescente')
        else:
            print('Crescente')


if __name__ == '__main__':
    main()