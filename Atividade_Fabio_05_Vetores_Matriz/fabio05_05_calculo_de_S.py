from tools_vetor import novo_vetor


def main():
    vetorA = novo_vetor(20)
    print('Valor de S eh: %.2f' % calculo_s(vetorA))


def calculo_s(vetor):
    valor_s = 0
    for i in range(len(vetor)):
        subtracao = (vetor[i] - vetor[((len(vetor))-1)-i])**2
        valor_s += subtracao
    
    return valor_s


if __name__ == '__main__':
    main()
