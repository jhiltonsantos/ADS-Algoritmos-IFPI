def main():
    valor_m, valor_n = map(int, input().split())
    soma(valor_m,valor_n)


def verifica_maior(valor_m, valor_n):
    m = valor_m
    n = valor_n
    
    if valor_n > valor_m:
        m = valor_n
        n = valor_m
    
    return m,n    


def soma(valor_m,valor_n):
    m,n = verifica_maior(valor_m,valor_n)
    
    while m > 0 and n > 0:
        soma = 0
        
        while n <= m:
            soma = soma + n
            print(n, end=' ')
            n += 1
        
        print('Sum={}'.format(soma))
        m,n = map(int, input().split())
        


if __name__ == '__main__':
    main()
