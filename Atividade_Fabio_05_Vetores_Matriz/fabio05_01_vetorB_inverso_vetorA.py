from tools_vetor import criar_vetor, inverter_vetor2


def main():
    quant_elementos = int(input('Quantidade de elementos: '))
    
    vetor_a = criar_vetor_A(quant_elementos)
    vetor_b = criar_vetor_B(vetor_a)

    print('Vetor de A: %s' % vetor_a)
    print('Vetor de B: %s' % vetor_b)


def criar_vetor_A(n):
    vetor = criar_vetor(n)
    for i in range(n):
        valor = int(input('Digite o valor: '))
        vetor[i] = valor

    return vetor


def criar_vetor_B(vetor):
    vetor_b = criar_vetor(len(vetor))
    
    for i in range(len(vetor)):
        vetor_b[i] = vetor[i]
    
    vetor_b = inverter_vetor2(vetor_b)

    return vetor_b


if __name__ == '__main__':
    main()