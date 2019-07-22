def main():
    valor_x = int(input('Valor de X: '))
    valor_n = int(input('Valor de N: '))
    
    divisao_de_x_por_n(valor_x,valor_n)
    

def divisao_de_x_por_n(x,n):
    while n > 2: 
        resultado = x / n
        
        print('Valor do resultado da divisao de %.2f'%x,\
            'por %.2f'%n,': %.2f'%resultado)
        
        x = resultado
        n -= 1
        if n <= 2:
            print('FIM DAS DIVISOES!!!')


if __name__ == '__main__':
    main()
