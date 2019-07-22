def main():
    vetor_quant = []
    vetor_quant += input().split()
    maior = ''
    while vetor_quant[0] != '0':
        quantidade, maior = (conta_letras(vetor_quant, maior))
        print(quantidade)
        vetor_quant.clear()
        vetor_quant += input().split()
        
    print('\nThe biggest word: %s' % maior)


def conta_letras(vetor, maior):
    quantidade = ''
    for i in range(len(vetor)):
        if i < (len(vetor)-1):
            quantidade += (str(len(vetor[i])) + '-')
        else:
            quantidade += (str(len(vetor[i])))
        
        if len(vetor[i]) >= len(maior):
            maior = vetor[i]
    
    return quantidade, maior 


main()