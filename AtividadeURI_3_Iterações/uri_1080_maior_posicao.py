def main():
    cont = 1
    lista = []

    while cont <= 100:
        valor = int(input())
        lista.append(valor)
        cont += 1
    
    maximo = max(lista)
    posicao = lista.index(maximo)
    print(maximo)
    print(posicao+1)


if __name__ == '__main__':
    main()