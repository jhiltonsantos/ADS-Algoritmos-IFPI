from tools_vetor import novo_vetor

def main():
    num_elementos = int(input('Digite o numero de elementos: '))
    vetor = novo_vetor(num_elementos)

    vetor_ordenado = ordenar_vetor(vetor)
    print('Vetor ordenado eh: %s' % vetor_ordenado)


def ordenar_vetor(vetor):
    maior = 0
    k = -1

    for i in range(len(vetor)):
        k += 1
        for j in range(k, len(vetor)):
            if vetor[i] > vetor[j]:
                maior = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = maior
    
    return vetor


if __name__ == '__main__':
    main()