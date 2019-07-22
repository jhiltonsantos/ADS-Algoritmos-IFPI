def main():
    valor = int(input())
    i = 1

    if 1 <= valor <= 1000:
        print(i)

        if valor % 2 == 0:
            valor -= 1

        while valor != i:
            i += 2
            print(i)


if __name__ == '__main__':
    main()
