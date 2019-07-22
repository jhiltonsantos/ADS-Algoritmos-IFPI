from tools_matriz import criar_matriz_com_valores, mostrar_matriz, criar_vetor


def main():
    ordem = int(input('Ordem da matriz: '))

    matriz = criar_matriz_com_valores(ordem, ordem)
    transposta = matriz_transposta(ordem, matriz)

    print('****Matriz Quadrada****')
    mostrar_matriz(matriz)
    print('\n***Matriz Transposta***')
    mostrar_matriz(transposta)


def matriz_transposta(n, matriz):
    transposta = criar_vetor()
    for i in range(n):
        linha = criar_vetor()
        for j in range(n):
            linha += [matriz[j][i]]
        transposta += [linha]
    
    return transposta


if __name__ == '__main__':
    main()