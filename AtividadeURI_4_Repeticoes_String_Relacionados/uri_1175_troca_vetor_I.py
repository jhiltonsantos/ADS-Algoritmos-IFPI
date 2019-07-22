def main():
    i = 0
    vetor = []
    while i < 20:
        valor = int(input())
        vetor.append(valor)
        i += 1
    
    v = inverte_vetor(vetor)
    for i in range(len(v)):
        print('N[%d] = %d' % (i, v[i]))
    

def inverte_vetor(vetor):
    inverte_vetor = []
    for i in range(len(vetor)):
        inverte_vetor.append(vetor[(len(vetor)-1)-i])
    
    return inverte_vetor


main()
