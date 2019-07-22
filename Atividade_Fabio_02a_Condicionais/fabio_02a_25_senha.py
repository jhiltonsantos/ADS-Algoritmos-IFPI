def main():
    senha = int(input('Digite a senha: '))
    
    if senha // 1000 == 0 or senha // 1000 > 9:
        print('Quantidade de digitos errada!')
    else:
        if senha == 1234:
            print('Acesso permitido!')
        else:
            print('Acesso negado!')


if __name__ == '__main__':
    main()
