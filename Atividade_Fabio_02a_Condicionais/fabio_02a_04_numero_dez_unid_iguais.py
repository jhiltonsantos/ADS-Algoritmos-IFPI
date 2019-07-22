def main():
    numero = int(input('Digite o numero de dois digitos: '))

    valor_1 = numero // 10
    valor_2 = numero % 10

    if numero > 99:
        print('Numero invalido')
    else:
        if valor_1 == valor_2:
            print('Numeros iguais')
        else:
            print('Numeros diferentes')


        
if __name__ == '__main__':
    main()