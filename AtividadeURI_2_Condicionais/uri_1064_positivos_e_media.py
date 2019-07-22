def main():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    num6 = float(input())
    numeros = [num1,num2,num3,num4,num5,num6]
    
    positivo(numeros)
    

def positivo(numeros):
    positivo_ver = []

    for i in numeros:
        if i > 0:
            positivo_ver.append(i)
    
    quant = len(positivo_ver)
    
    print('{} valores positivos'.format(len(positivo_ver)))
    media(quant, positivo_ver)    
    

def media(quant, lista):
    soma = 0
    
    for valor_lista in lista:
        soma = soma + valor_lista
    
    if quant > 0:
        media = soma / quant
        print('{:.1f}'.format(media))


if __name__ == '__main__':
    main()
