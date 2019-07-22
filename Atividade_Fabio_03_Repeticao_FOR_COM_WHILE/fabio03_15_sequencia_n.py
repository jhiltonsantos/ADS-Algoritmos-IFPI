def main():
    valor = int(input('Valor de N: '))
    cont = 1
    x = 1
    print(cont, end=' ')

    while cont <= valor:
        sequencia = x+1
        x = cont + sequencia
        
        print(x, end=' ')
        cont += 1 


if __name__ == '__main__':
    main()