from tools_vetor import criar_vetor


def main():
    num_elementos = int(input('Digite o numero de elementos: '))
    
    print('Sequencia de Fibonnaci: %s.' % fibonacci_vetor(num_elementos))


def fibonacci_vetor(n):
    vetor = criar_vetor(n)
    vetor[1] = 1
    
    for i in range(2, n):
        vetor[i] = vetor[i-2] + vetor[i-1]

    return vetor


if __name__ == '__main__':
    main()