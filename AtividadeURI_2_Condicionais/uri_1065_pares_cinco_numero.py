def main():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    numeros = [num1,num2,num3,num4,num5]
    
    pares(numeros)


def pares(numeros):
    valor_par = []

    for par in numeros:
        if par % 2 == 0:
            valor_par.append(par)
    
    print('{} valores pares'.format(len(valor_par)))
    

if __name__ == '__main__':
    main()
