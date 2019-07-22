from tools_vetor import *


def criar_matriz(linhas, colunas):
    matriz = criar_vetor(linhas)
    for i in range(linhas):
        matriz[i] = criar_vetor(colunas)
    return matriz


def criar_matriz_com_valores(linhas, colunas):
    matriz = criar_vetor()
    for i in range(linhas):
        linha = criar_vetor()
        for j in range(colunas):
            linha += [int(input('Digite o valor %d na linha %d: ' % ((j+1), (i+1))))]
        matriz += [linha]
    
    return matriz


def matriz_transposta(n, matriz):
    transposta = criar_vetor()
    for i in range(n):
        linha = criar_vetor()
        for j in range(n):
            linha += [matriz[j][i]]
        transposta += [linha]
    
    return transposta


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()


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