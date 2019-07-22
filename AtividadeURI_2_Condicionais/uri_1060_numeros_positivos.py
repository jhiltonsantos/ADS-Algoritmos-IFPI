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
    
    print('{} valores positivos'.format(len(positivo_ver)))
    

if __name__ == '__main__':
    main()
