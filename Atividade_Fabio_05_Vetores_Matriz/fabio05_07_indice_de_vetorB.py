from tools_vetor import novo_vetor, criar_vetor


def main():
    quant_elementos = int(input('Digite a quantidade de elementos: '))
    vetorA = novo_vetor(quant_elementos)
    vetorB = indice_vetorB(quant_elementos)

    print('Elementos de A: %s' % vetorA)
    print('Elementos de B: %s' % vetorB)


def indice_vetorB(n):
    vetor = criar_vetor(n)

    for i in range(len(vetor)):
        if i % 2 == 0:
            vetor[i] = 0
        else: 
            vetor[i] = 1
    
    return vetor


if __name__ == '__main__':
    main()