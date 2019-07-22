def main():
    valor_n = int(input())
    cont = 1

    while cont <= valor_n:
        x,y = map(int, input().split())
        if y==0:
            resultado = 'divisao impossivel'
        elif x == 0:
            resultado = 0.0
        else:
            resultado = x / y

        print(resultado)
        cont += 1


if __name__ == '__main__':
    main()