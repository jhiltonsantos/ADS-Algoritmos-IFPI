def main():
    numero_coluna = int(input())
    operacao = input()
    matriz = criar_matriz_com_valores()
    
    if operacao == 'S':
        print('%.1f' % soma_coluna(matriz, numero_coluna))
    elif operacao == 'M':
        print('%.1f' % media_coluna(matriz, numero_coluna))


def criar_matriz_com_valores(linhas=12, colunas=12):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha += [float(input())]
        matriz += [linha]
    
    return matriz


def soma_coluna(matriz, coluna):
    soma = 0
    for i in range(len(matriz[0])):
        soma += matriz[i][coluna]

    return soma


def media_coluna(matriz, coluna):
    soma = soma_coluna(matriz, coluna)
    tamanho_linha = len(matriz[0])
    
    return (soma / tamanho_linha)


if __name__ == '__main__':
    main()
