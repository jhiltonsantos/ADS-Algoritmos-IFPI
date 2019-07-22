def main():
    matriz = criar_matriz()
    print('**************** MATRIZ ****************')
    mostrar_matriz(matriz)
    print()

    soma_matriz = soma_total_matriz(matriz)
    print('Soma de todos os elementos na matriz: %.2f.\n' % soma_matriz)
    
    media_impar = media_coluna_impar(matriz)
    print('Media dos elementos nas colunas impares: %.2f.\n' % media_impar)
    
    maior_elemento = maior_valor_diagonal(matriz)
    print('Maior elemento da matriz: %.2f.\n' % maior_elemento)
    
    print('*****ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL*******')
    valores_acima_da_diagonal_principal(matriz)

    soma_abaixo_diag_principal = soma_elementos_abaixo_diagonal_principal(matriz)
    print('Soma dos elementos abaixo da diagonal principal da matriz: %s.\n'\
         % soma_abaixo_diag_principal)
    
    print('***POSICAO DO ELEMENTO DENTRO DA MATRIZ***')
    print('Posicao na Matriz: %s' % verifica_posicao_multiplo(matriz))


def criar_vetor(tamanho, valor_inicial=0):
    return [valor_inicial] * tamanho


def criar_matriz():
    matriz = criar_vetor(10)
    index = 0

    for i in range(len(matriz)):
        linha = criar_vetor(10)
        for j in range(len(linha)):
            linha[j] = ('%.2f' % index)
            index += 0.15
        matriz[i] = linha

    return (matriz)


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()


def soma_total_matriz(matriz):
    somatorio = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            somatorio += float(matriz[i][j])
    
    return somatorio


def soma_elementos_abaixo_diagonal_principal(matriz):
    somatorio = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i > j:
                somatorio += float(matriz[i][j])

    return somatorio


def media_coluna_impar(matriz):
    soma = 0
    quantidade = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j % 2 != 0:
                soma += float(matriz[j][i])
                quantidade += 1 
    
    return (soma/quantidade)


def maior_valor_diagonal(matriz):
    maior = 0.0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                if float(matriz[i][j]) > maior:
                    maior = float(matriz[i][j])

    return maior


def valores_acima_da_diagonal_principal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                print(matriz[i][j], end=' ')
        print()


def verifica_posicao_multiplo(matriz):
    numero = float(input('Digite o multiplo de 0.15: '))
    posicao = posicao_na_matriz(numero, matriz)

    return posicao


def posicao_na_matriz(numero, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if float(matriz[i][j]) == numero:
                linha = i
                coluna = j
    
    if (linha==coluna) and ((linha+coluna)==len(matriz[linha])-1):
        return 'Centro da Matriz.'
    elif (linha == coluna):
        return 'Diagonal Principal.'
    elif (linha+coluna) == (len(matriz[linha])-1):
        return 'Diagonal Secundaria.'
    elif  linha > coluna:
        return 'Abaixo da Diagonal Principal.'
    elif linha < coluna:
        return 'Acima da Diagonal Principal.'


if __name__ == '__main__':
    main()