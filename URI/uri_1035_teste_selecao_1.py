def main():
    dados = input().split(" ")
    A, B, C, D = map(int, dados)

    if ((B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0)):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')


if __name__ == '__main__':
        main()
