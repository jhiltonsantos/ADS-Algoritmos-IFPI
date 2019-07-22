from tools_vetor import novo_vetor

def main():
    num_elementos = int(input('Digite o numero de elementos: '))
    vetor = novo_vetor(num_elementos)
    maior_elemento, menor_elemento = comparar_elemento(vetor)
    
    print('O maior elementos eh: %d.\nE o menor: %d.'\
         % (maior_elemento, menor_elemento))


def comparar_elemento(vetor):
    maior = vetor[0]
    menor = maior

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]
    
    return maior, menor


if __name__ == '__main__':
    main()