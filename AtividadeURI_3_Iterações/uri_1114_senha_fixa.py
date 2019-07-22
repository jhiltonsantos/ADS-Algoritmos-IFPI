def main():
    senha = 0

    while senha != 2002:
        senha = int(input())

        if senha != 2002:
            print('Senha Invalida')
        else:
            print('Acesso Permitido')


if __name__ == '__main__':
    main()
    