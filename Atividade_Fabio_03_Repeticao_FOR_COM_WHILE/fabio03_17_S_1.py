def main():
    valor_n = int(input('Digite o valor de N: '))
    
    print('Resultado = %.2f' % calculo_s(valor_n))


def calculo_s(n):
    cont = 1
    soma = 0
    while cont <= n:
        calculo = (1/cont)
        soma = soma + calculo
        cont += 1
    return soma
        

if __name__ == '__main__':
    main()
