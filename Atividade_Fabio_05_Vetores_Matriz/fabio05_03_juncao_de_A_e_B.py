from tools_vetor import criar_vetor


def main():
    quant_elementos = int(input('Quantidade de elementos: '))

    vetorA = novo_vetor(quant_elementos)
    vetorB = novo_vetor(quant_elementos)
    
    print('Juncao dos vetores: %s' % juncao_de_vetores(vetorA, vetorB))
    

def novo_vetor(n):
    vetor = criar_vetor(n)
    for i in range(n):
        vetor[i] += int(input('Valor %d: ' % (i+1)))

    return vetor


def juncao_de_vetores(vetor1, vetor2):
    tamanho = len(vetor1) + len(vetor2)
    vetorC = criar_vetor(tamanho)
    
    for i in range(len(vetor1)):
        vetorC[i] = vetor1[i]
    
    k = 0
    for j in range(len(vetor1), tamanho):    
        while k <= len(vetor2):
            vetorC[j] = vetor2[k]
            k += 1
            break
            
    return vetorC


if __name__ == '__main__':
    main()