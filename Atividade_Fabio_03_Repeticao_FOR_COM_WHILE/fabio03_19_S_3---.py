def main():
    valor_n = int(input('Digite o valor de N: '))
    
    print('Resultado: %.2f'%calculo(valor_n))
    

def calculo(n):
    cont = 1
    soma = 0
    
    while cont <= n:
        
        if cont % 2 ==0:
            calc = ((n-(cont-1))/cont)
        else:
            if cont == 1:
                calc = (1/n)
            else:
                calc=(cont/(n-(cont-1)))
        soma = soma + calc
        cont +=1
    
    return soma

if __name__ == '__main__':
    main()
    