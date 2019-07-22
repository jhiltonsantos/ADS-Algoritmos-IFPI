def main():
    valor_n = int(input('Numero: '))
    cont = 1

    while cont**2 <= valor_n:
        quadrado = cont ** 2
        cont +=1
    
    print('Valor ao quadrado mais proximo do numero: ',quadrado)


if __name__ == '__main__':
    main()
