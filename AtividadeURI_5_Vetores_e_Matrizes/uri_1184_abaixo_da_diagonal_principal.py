def main():
    operacao = input()
    matriz = criar_matriz_com_valores()
    
    if operacao == 'S':
        print('%.1f' % (soma_matriz(matriz)))
    elif operacao == 'M':
        print('%.1f' % (media_matriz(matriz)))
        

def criar_matriz_com_valores(linhas=12, colunas=12):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha += [float(input())]
        matriz += [linha]
    
    return matriz


# DIFERENCA QUE INVERTE O MAIOR QUE (>)  
# [i > j] →→ Abaixo da Diagonal principal
# [i < j] →→ Acima da Diagonal principal

def soma_matriz(matriz):
    soma = 0
    for i in range(12):
        for j in range(12):
            if i > j:
                soma += matriz[i][j]

    return soma


def tamanho_elementos_abaixo_da_diagonal(matriz):
    tamanho = 0
    for i in range(1, len(matriz[0])):
        tamanho += len(matriz[0]) - i
    
    return tamanho


def media_matriz(matriz):
    return (soma_matriz(matriz)/tamanho_elementos_abaixo_da_diagonal(matriz))


if __name__ == '__main__':
    main()
