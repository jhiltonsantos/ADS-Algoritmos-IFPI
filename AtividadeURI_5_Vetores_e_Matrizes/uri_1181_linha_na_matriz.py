def main():
    numero_linha = int(input())
    operacao = input()
    matriz = criar_matriz_com_valores()
    
    if operacao == 'S':
        print('%.1f' % soma_linha(matriz, numero_linha))
    elif operacao == 'M':
        print('%.1f' % media_linha(matriz, numero_linha))


def criar_matriz_com_valores(linhas=12, colunas=12):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha += [float(input())]
        matriz += [linha]
    
    return matriz


def soma_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[0])):
        soma += matriz[linha][i]

    return soma


def media_linha(matriz, linha):
    soma = 0
    tamanho_linha = len(matriz[0])
    for i in range(tamanho_linha):
        soma += matriz[linha][i]

    return (soma/tamanho_linha)


if __name__ == '__main__':
    main()
