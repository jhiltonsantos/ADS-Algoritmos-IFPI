def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    numeros = [num1,num2,num3,num4,num5]
    
    pares(numeros)
    impar(numeros)
    positivo(numeros)
    negativo(numeros)


def pares(numeros):
    valor_par = []

    for n in numeros:
        if n % 2 == 0:
            valor_par.append(n)
    
    print('{} valor(es) par(es)'.format(len(valor_par)))


def impar(numeros):
    valor_impar = []

    for n in numeros:
        if n % 2 != 0:
            valor_impar.append(n)
    
    print('{} valor(es) impar(es)'.format(len(valor_impar)))


def positivo(numeros):
    valor_positivo = []

    for n in numeros:
        if n > 0:
            valor_positivo.append(n)
    
    print('{} valor(es) positivo(s)'.format(len(valor_positivo)))
    

def negativo(numeros):
    valor_negativo = []

    for n in numeros:
        if n < 0:
            valor_negativo.append(n)
    
    print('{} valor(es) negativo(s)'.format(len(valor_negativo)))
    

if __name__ == '__main__':
    main()
