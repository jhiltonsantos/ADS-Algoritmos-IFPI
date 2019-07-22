def main():
    
    i = 0
    vetor = []
    while i < 10:
        vetor += [int(input())]
        
        if vetor[i] <= 0:
            vetor[i] = 1

        print('X[%d] = %d' % (i, vetor[i]))
        i += 1


main()