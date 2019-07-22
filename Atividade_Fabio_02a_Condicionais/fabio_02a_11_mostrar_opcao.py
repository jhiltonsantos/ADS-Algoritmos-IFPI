def main():
    opcao = int(input("Opcao: "))
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    numero_3 = int(input("Numero 3: "))

    if 0 < opcao <= 3:
        if opcao == 1:
            print(numero_1)
        elif opcao == 2:
            print(numero_2)
        elif opcao == 3:
            print(numero_3)
    else:
        print('Opcao invalida')


if __name__ == '__main__':
    main()