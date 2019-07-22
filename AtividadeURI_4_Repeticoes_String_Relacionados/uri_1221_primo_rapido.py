import time

def main():
    inicio = time.time()
    quant_test = int(input())
    
    for i in range(quant_test):
        numero = int(input())
        print(eh_primo(numero))

    fim = time.time()
    print(fim-inicio)


'''def eh_primo(numero):
    raiz = int(numero ** (1/2))

    if numero <= 1:
        return 'Not Prime'
    else:
        for i in range (2, numero):
            if numero % raiz == 0:
                return 'Not Prime'
        return 'Prime
'''

'''
def eh_primo(numero):
    raiz = int(numero ** (1/2))
    
    while raiz > 1:
        if numero % raiz == 0:
            return 'Not Prime'
        raiz -= 1
    
    return 'Prime'


if __name__ == '__main__':
    main()