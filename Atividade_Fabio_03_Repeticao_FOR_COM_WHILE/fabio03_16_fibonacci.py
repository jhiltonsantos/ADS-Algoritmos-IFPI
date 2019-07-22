def main():
    valor = int(input('Valor de N: '))
    
    while valor < 2:
        valor = int(input('Valor de N: '))
    
    imprimir(valor)


def fibonacci(valor):
    if valor == 0:
        sequencia = 0
    elif valor == 1:
        sequencia = 1
    else:
        sequencia = fibonacci(valor-1) + fibonacci(valor-2)

    return sequencia


def imprimir(valor):
    cont = 0
    
    while cont < valor:
        print(fibonacci(cont), end=' ')
        cont += 1



if __name__ == '__main__':
    main()