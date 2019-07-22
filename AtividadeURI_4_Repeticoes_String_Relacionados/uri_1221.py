def main():
    quant_test = input()
    quant_test = int(quant_test)
        
    for i in range(quant_test):
        numero = input()
        numero = int(numero)
        
        if sieve:
            print('Prime')
        else:
            print('Not Prime')


def sieve(numero):
    
    vetor = [True] * (numero+1)
    vetor[1] = False
    vetor[0] = vetor[1]

   

main()