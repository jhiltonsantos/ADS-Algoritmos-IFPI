from tools_vetor import criar_vetor


def main():
    quant_elementos = int(input('Quantidade de elementos: '))

    vetorA = criar_vetor_A(quant_elementos)
    print('Vetor: %s' % vetorA)

    if existe_ou_nao_elementos_iguais(vetorA):
        print('Elementos iguais no vetor')
    else:
        print('Não existe elementos iguais no vetor')
    

def criar_vetor_A(n):
    vetor = criar_vetor(n)
    for i in range(n):
        valor = int(input('Digite o valor: '))
        vetor[i] = valor

    return vetor


def existe_ou_nao_elementos_iguais(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if (i!=j) and (vetor[i] == vetor[j]):
                return True
    return False


main()