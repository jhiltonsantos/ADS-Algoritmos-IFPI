def main():
    valor = int(input())

    while valor != 0:
        matriz = criar_matriz(valor, valor)
        for i in range(valor):
            for j in range(valor):
                print(matriz[i][j])
        valor = int(input())


def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha += [1]
        matriz += [linha]
    
    return matriz


if __name__ == '__main__':
    main()