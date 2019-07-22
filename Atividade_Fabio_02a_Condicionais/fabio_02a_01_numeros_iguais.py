def main():
    # entrada
    num_1 = int(input('Numero 1: '))
    num_2 = int(input('Numero 2: '))
    num_3 = int(input('Numero 3: '))
    
    # saida
    if num_1 == num_2 == num_3:
        print('Os tres sao iguais!!!')
    elif num_1 == num_2 and num_3 != num_1:
        print('Dois numeros iguais!!!')
    elif num_1 == num_3 and num_2 != num_1:
        print('Dois numeros iguais!!!')
    elif num_2 == num_3 and num_2 != num_1:
        print('Dois numeros iguais!!!')
    else:
        print('Nenhum dos numeros sao iguias!!!')


if __name__ == '__main__':
    main()