from tools_vetor import criar_vetor, novo_vetor, juncao_de_vetores, contem


def main():
    quant = int(input('Quantidade de elementos no vetor: '))
    vetorA = novo_vetor(quant)
    vetorB = novo_vetor(quant)

    vetorC = uniao_de_vetor(vetorA, vetorB)
    vetorD = intersecao_de_vetor(vetorA, vetorB)

    print('A uniao dos vetores eh: %s\nA intersecao eh: %s' % (vetorC, vetorD))


def uniao_de_vetor(vetor1, vetor2):
    #  União é todos os elementos dos conjuntos sem repetir nenhum elemento
    tamanho = len(vetor1) + len(vetor2)
    vetor_juncao = criar_vetor(tamanho)
    vetor_juncao = juncao_de_vetores(vetor1, vetor2)
    
    vetor_uniao = criar_vetor()
    for i in range(len(vetor_juncao)):
        if contem(vetor_uniao, vetor_juncao[i]):
            vetor_uniao += [vetor_juncao[i]] 

    return vetor_uniao


def intersecao_de_vetor(vetor1, vetor2):
    #  Intersecao é os elementos comuns dos conjuntos
    vetor_intersecao = criar_vetor()

    for i in range(len(vetor1)):
        if not(contem(vetor2, vetor1[i])):
            vetor_intersecao += [vetor1[i]]
    
    return vetor_intersecao


if __name__ == '__main__':
    main()