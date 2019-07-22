def criar_vetor(tamanho=0, valor_inicial=0):
    vetor = [valor_inicial] * tamanho
    
    return vetor


def novo_vetor(n):
    vetor = criar_vetor(n)
    for i in range(n):
        vetor[i] += float(input('Valor %d: ' % (i+1)))

    return vetor


def add_vetor(n, valor):
    vetor = criar_vetor(n)
    diferenca = len(vetor) - len(valor)
    
    if diferenca > 0:
        for i in range(diferenca):
            vetor[i] = '0'
    
        for i in range(diferenca, len(vetor)):
            vetor[i] = valor[i - diferenca]
    elif diferenca < 0:
        return False
    else:
        for i in range(len(vetor)):
            vetor[i] = valor[i]    
        
    return vetor


def inverter_vetor(vetor):
    return vetor[::-1]


def inverter_vetor2(vetor):
    vetorA = []
    for i in range(len(vetor)):
        vetorA += [vetor[(len(vetor)-1)-i]]
    
    return vetorA


def juncao_de_vetores(vetor1, vetor2):
    tamanho = len(vetor1) + len(vetor2)
    vetor = criar_vetor(tamanho)
    
    for i in range(len(vetor1)):
        vetor[i] = vetor1[i]

    for i in range(len(vetor2)):
        vetor[len(vetor1)+i] = vetor2[i]

    return vetor


def contem(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return False
    return True


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


def fibonacci_vetor(n):
    vetor = criar_vetor(n)
    vetor[0] = 0
    vetor[1] = 1
    
    for i in range(2, n):
        vetor[i] = vetor[i-2] + vetor[i-1]

    return vetor


# Juntar dois vetores invertendo o segundo
def juncao_de_vetores_com_inverso_segundo(vetor1, vetor2):
    tamanho = len(vetor1) + len(vetor2)
    vetorC = criar_vetor(tamanho)
    print(tamanho)

    for i in range(len(vetor1)):
        vetorC[i] = vetor1[i]
    
    for j in range(len(vetor1), tamanho):
        vetorC[j] = vetor2[(tamanho-1) - j]
        
    return vetorC
