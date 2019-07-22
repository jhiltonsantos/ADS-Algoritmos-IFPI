def main():
    limite_inferior = int(input('Digite o valor inicial: '))
    limite_superior = int(input('Digite o valor final: '))
    divisor = 1
    
    while limite_inferior <= limite_superior:
        if not(limite_inferior % divisor == 0):
            print(limite_inferior, end=' ')
        else:
            break
        
        divisor += 1      
        limite_inferior += 1


if __name__ == '__main__':
    main()