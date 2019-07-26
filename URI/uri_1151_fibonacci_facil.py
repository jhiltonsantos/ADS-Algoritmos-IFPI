def main():
    numero = int(input())

    a = 0
    b = 1
    for i in range(numero):
        if i+1 == numero:
            print(a)
        else:
            print(a, end=' ')
        a, b = b, a+b


main()