def main():
    valor_n = int(input('Digite o valor de N: '))
    
    print('Resultado: %.2f'%calculo(valor_n))
    

def calculo(n):
    cont = 1
    soma = 0
    
    while cont <= n:
        calculo = 1/cont
        if cont % 2 ==0:
            soma = soma - calculo
        else:
            soma = soma + calculo
        cont +=1
    
    return soma

if __name__ == '__main__':
    main()
    