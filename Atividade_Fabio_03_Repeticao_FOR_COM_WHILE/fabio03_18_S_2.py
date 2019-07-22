def main():
    valor_n = int(input('Digite o valor de N: '))
    print('Resultado: %.2f'%calculo(valor_n))

def calculo(n):
    cont = 1
    soma = 0

    while cont <= n:
        if cont == 1:
            divisao_fracao = (cont/(n))
        elif cont == 2:
            divisao_fracao = (cont/(n-1))
        else:
            divisao_fracao = (cont/(n-(cont-1)))
    
        soma += divisao_fracao
        cont += 1 

    ultima_fracao = (n/1)
    resultado = soma + ultima_fracao
    
    return resultado 

if __name__ == '__main__':
    main()