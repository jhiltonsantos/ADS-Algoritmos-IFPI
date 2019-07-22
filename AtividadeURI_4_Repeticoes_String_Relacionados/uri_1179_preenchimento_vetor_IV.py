def main():
    vetor_par = []
    vetor_impar = []
    resultado(vetor_impar,vetor_par)    


def leia(vetor_impar, vetor_par, j, l):
    valor = int(input())
    if valor%2 == 0:
        vetor_par += [valor]
        j += 1
    else:
        vetor_impar += [valor]
        l += 1
    
    return vetor_impar, vetor_par, j, l


def resultado(vetor_impar, vetor_par):
    j = 0
    l = 0

    for i in range(15):
        ##
        vetor_impar, vetor_par, j, l = leia(vetor_impar, vetor_par, j, l)

        if len(vetor_par) >= 5:
            print('par[%d] = %s' % ((j-5), vetor_par[j-5]))
            print('par[%d] = %s' % ((j-4), vetor_par[j-4]))
            print('par[%d] = %s' % ((j-3), vetor_par[j-3]))
            print('par[%d] = %s' % ((j-2), vetor_par[j-2]))
            print('par[%d] = %s' % ((j-1), vetor_par[j-1]))
            vetor_par.clear()
            j = 0
        
        if len(vetor_impar) >= 5:
            print('impar[%d] = %s' % ((l-5), vetor_impar[l-5]))
            print('impar[%d] = %s' % ((l-4), vetor_impar[l-4]))
            print('impar[%d] = %s' % ((l-3), vetor_impar[l-3]))
            print('impar[%d] = %s' % ((l-2), vetor_impar[l-2]))
            print('impar[%d] = %s' % ((l-1), vetor_impar[l-1]))
            vetor_impar.clear()
            l = 0

    restante(vetor_impar, vetor_par)
    
    
def restante(vetor_impar, vetor_par):
    if len(vetor_impar) > 0:
        for i in range(len(vetor_impar)):
            print('impar[%d] = %s' % ((i), vetor_impar[i]))

    if len(vetor_par) > 0:
        for i in range(len(vetor_par)):
            print('par[%d] = %s' % ((i), vetor_par[i]))


main()